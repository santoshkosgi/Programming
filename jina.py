"""
The idea is to make a list of function calls that needs to be called for availability and Price fetching services.
Trigger these functions asynchronously and sort the available items based on price.
As, we need to sort only available items, we have tried following two approaches:
1. Calling price fetching service only for available items.
2. Calling price fetching service for all the items and sorting on the available items.

Intuitively the first case should perform well. But till certain number of item_ids second case performs well.
This might be because of asynchronously calling lot of functions is computationally efficient than fetching price
only for available items till some number of items(This is also based on the time taken by availability and
price fetching service)

Following are some results:

Length of Items    Fetching price for only available items    Fetching price for all Items
     100	                   0.2031955719	                         0.1021785736
     1000	                   0.2090339661	                         0.1117343903
     10000	                   0.2447009087	                         0.1599185467
     100000	                   0.3954846859	                         0.3775389194
     1000000	               2.469397545	                         3.11268878
     10000000	               29.42602348	                         37.89828563

Second and thrid column contains time taken in seconds.
"""
import asyncio

from typing import List
from itertools import chain
from dataclasses import dataclass

MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL = 100
MAX_LIST_OF_ITEM_IDS_PRICING_CALL = 150


@dataclass
class PricedItem:
    item_id: str
    selling_price: float
    discount: bool


async def consult_item_available(item_ids: List[str]) -> List[bool]:
    """
    Checks for a batch of item_ids if each of them are available or not

    :param item_ids: List of IDs of the items for which we need to know the availability
    :return: List of booleans indicating the availability of each ID in item_ids

        .. note:
            The service does not accept a list longer than MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL
    """
    import random
    assert len(item_ids) <= MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL
    await asyncio.sleep(0.1)
    # backend logic from the server
    return [bool(random.randint(0, 1)) for _ in item_ids]


async def consult_price(item_ids: List[str]) -> List[PricedItem]:
    """
    Returns a list of :class:PricedItem for each of the requested item_ids


    :param item_ids: List of IDs of the items for which we need to know the pricing information
    :return: List of :class:PricedItem for each of the item_ids

        .. note:
            The service does not accept a list longer than MAX_LIST_OF_ITEM_IDS_PRICING_CALL
    """
    import random
    assert len(item_ids) <= MAX_LIST_OF_ITEM_IDS_PRICING_CALL
    await asyncio.sleep(0.1)
    # backend logic from the server
    return [PricedItem(item_id, random.random(), bool(random.randint(0, 1))) for item_id in item_ids]


def get_func_calls(item_ids: List[str], max_per_call: int, func_name):
    num_of_func_calls = int(len(item_ids)/max_per_call)

    if len(item_ids) % max_per_call != 0:
        num_of_func_calls += 1

    start_index = 0
    func_calls = []

    for call_index in range(num_of_func_calls):
        func_calls.append(func_name(
            item_ids=item_ids[start_index: start_index + max_per_call]))
        start_index += max_per_call

    return num_of_func_calls, func_calls


async def return_top_cheapest_items(item_ids: List[str], top_k: int):
    """
    Function that receives a list of item IDs and a top_k parameter, and returns a list of item_ids that are available and sorted from cheapest to most expensive

    :param item_ids: The list of item IDs that are candidates to be returned
    :param top_k: The amount of item IDs to be returned
    """
    # Collecting async function calls

    num_availiablity_func_calls, func_calls = get_func_calls(
        item_ids=item_ids, max_per_call=MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL,
        func_name=consult_item_available)

    # Calling consult_item_available first
    result = await asyncio.gather(*func_calls, return_exceptions=True)
    availiable_items = []

    for index, result_item in enumerate(result):
        if type(result_item) is not list:
            continue
        for i, is_avail in enumerate(result_item):
            if is_avail is True:
                availiable_items.append(item_ids[MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL*index + i])

    func_calls = []

    # Choosing only the aviliable items
    item_ids = availiable_items
    num_price_check_func_calls, func_calls = get_func_calls(
        item_ids=item_ids, max_per_call=MAX_LIST_OF_ITEM_IDS_PRICING_CALL,
        func_name=consult_price)

    result = await asyncio.gather(*func_calls, return_exceptions=True)

    price_list = []

    for index, result_item in enumerate(result):
        if type(result_item) is not list:
            continue
        price_list.extend(result_item)

    availiable_items = price_list

    # Sorting  based on item price
    availiable_items = sorted(availiable_items, key=lambda x: (x.selling_price, int(x.discount)))
    availiable_items = availiable_items[:top_k]
    result = [item.item_id for item in availiable_items]
    return result


async def return_top_cheapest_items_check_price_of_all_items(item_ids: List[str], top_k: int):
    """
    Function that receives a list of item IDs and a top_k parameter, and returns a list of item_ids that are available
    and sorted from cheapest to most expensive.
    This function checks price of all items and sorts only items which are availiable.

    :param item_ids: The list of item IDs that are candidates to be returned
    :param top_k: The amount of item IDs to be returned
    """

    num_availiablity_func_calls, func_calls_avail = get_func_calls(
        item_ids=item_ids, max_per_call=MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL,
        func_name=consult_item_available)

    num_price_check_func_calls, func_calls_price = get_func_calls(
        item_ids=item_ids, max_per_call=MAX_LIST_OF_ITEM_IDS_PRICING_CALL,
        func_name=consult_price)

    func_calls = func_calls_avail + func_calls_price

    result = await asyncio.gather(*func_calls)
    # Handle Exceptions
    availiable_items = []

    for index, result_item in enumerate(result[0:num_availiablity_func_calls]):
        if type(result_item) is not list:
            availiable_items.extend([False] * MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL)
            continue
        availiable_items.extend(result_item)

    availiability_list = availiable_items

    # Handle Exceptions
    price_list = []
    for index, result_item in enumerate(result[num_availiablity_func_calls:]):
        if type(result_item) is not list:
            price_list.extend([None] * MAX_LIST_OF_ITEM_IDS_PRICING_CALL)
            continue
        price_list.extend(result_item)

    availiable_items = []

    for is_avail, item_price in zip(availiability_list, price_list):
        if is_avail is True:
            availiable_items.append(item_price)

    # Sorting  based on item price
    availiable_items = sorted(availiable_items, key=lambda x: (x.selling_price, int(x.discount)))
    availiable_items = availiable_items[:top_k]
    result = [item.item_id for item in availiable_items]
    return result


def unit_test():
    import random
    items = [str(i) for i in range(1000)]
    random.seed(34)
    assert asyncio.run(return_top_cheapest_items(items, 10)) == ['604', '871', '843', '690', '983', '844', '68', '784', '97', '870']
    random.seed(43)
    assert asyncio.run(return_top_cheapest_items_check_price_of_all_items(items, 10)) == ['181', '880', '295', '250', '802', '396', '201', '12', '672', '661']

    print("Test Cases Passed :)")


if __name__ == '__main__':
    import time
    top_k = 10
    items = [str(i) for i in range(1000)]
    begin = time.time()
    print(asyncio.run(return_top_cheapest_items_check_price_of_all_items(items, top_k)))
    end = time.time()
    print(f"Total runtime of the program computing price of only availiable items is {end - begin}")
    # for num_of_items in [100, 1000, 10000, 100000, 1000000, 10000000]:
    #     items = [str(i) for i in range(num_of_items)]
    #     begin_1 = time.time()
    #     asyncio.run(return_top_cheapest_items(items, top_k))
    #     end_1 = time.time()
    #     # print(f"Total runtime of the program computing price of only availiable items is {end - begin}")
    #
    #     begin_2 = time.time()
    #     asyncio.run(return_top_cheapest_items_2(items, top_k))
    #     end_2 = time.time()
    #     print(num_of_items, ", ", end_1 - begin_1, ", ", end_2 - begin_2)
    #     # print(f"Total runtime of the program computing price of all items is {end - begin}")
