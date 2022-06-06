# import asyncio
#
# # A co-routine
# async def add(x: int, y: int):
#     return x + y
#
# # Create a function to schedule co-routines on the event loop
# # then print results
# async def get_results():
#     inputs = [(2,3), (4,5), (5,5), (7,2)]
#
#     # Create a co-routine list
#     cors = [add(x,y) for x,y in inputs]
#     results = asyncio.gather(*cors)
#
#     print(await results) # Prints [5, 9, 10, 9]
#
# asyncio.run(get_results())


"""
We are an e-commerce company, and we have to write a service whose job will be to return the `top_k` items. `top_k` here means the `k` cheapest items. This list should be sorted from cheapest to most expensive.

To support the service, we have to call 2 other external services managed by other teams in the company.

- Availability service (consult_item_available) is a service mantained by the operations team, that returns information about the stock availability of a given item

- Pricing service (consult_price) is a service mantained by the pricing team, that knows the exact price applicable for each item at a given time, and whether it is discounted or not.

The interface with the Availability Service is clear because it returns a simple boolean for each item indicating its availability.
With the pricing team, we have agreed on encapsulating the response in a class `PricedItem` where the selling price and the discount flag is filled.

Both services can process in a single call as much as MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL and MAX_LIST_OF_ITEM_IDS_PRICING_CALL for a single request.

The job of the team is to provide a service that returns the list of top_k items that are available. The list should be sorted from cheapest to most expensive. The product manager
also told us that they would like to promote better discounted items, because they plan to show a special badge in the frontend.

    ..note:
        `consult_item_available` and `consult_price` are shown for clarity, but the exact implementation is unknown,
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


async def return_top_cheapest_items(item_ids: List[str], top_k: int):
    """
    Function that receives a list of item IDs and a top_k parameter, and returns a list of item_ids that are available and sorted from cheapest to most expensive

    :param item_ids: The list of item IDs that are candidates to be returned
    :param top_k: The amount of item IDs to be returned
    """
    func_calls = []

    num_availiablity_func_calls = int(len(item_ids)/MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL)
    if len(item_ids) % MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL != 0:
        num_availiablity_func_calls += 1
    start_index = 0
    for call_index in range(num_availiablity_func_calls):
        func_calls.append(consult_item_available(
            item_ids=item_ids[start_index: start_index+MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL]))
        start_index += MAX_LIST_OF_ITEM_IDS_AVAILABILITY_CALL

    # Calling consult_item_available first
    result = await asyncio.gather(*func_calls)
    availiability_list = list(chain.from_iterable(result[0:num_availiablity_func_calls]))

    availiable_items = [None] * sum(availiability_list)

    start_index = 0
    for index, is_avail in enumerate(availiability_list):
        if is_avail is True:
            availiable_items[start_index] = item_ids[index]
            start_index += 1

    func_calls = []

    # Choosing only the aviliable items
    item_ids = availiable_items

    num_price_check_func_calls = int(len(item_ids) / MAX_LIST_OF_ITEM_IDS_PRICING_CALL)
    if len(item_ids) % MAX_LIST_OF_ITEM_IDS_PRICING_CALL != 0:
        num_price_check_func_calls += 1
    start_index = 0
    for call_index in range(num_price_check_func_calls):
        func_calls.append(consult_price(
            item_ids=item_ids[start_index: start_index + MAX_LIST_OF_ITEM_IDS_PRICING_CALL]))
        start_index += MAX_LIST_OF_ITEM_IDS_PRICING_CALL

    result = await asyncio.gather(*func_calls)
    # availiability_list = list(chain.from_iterable(result[0:num_availiablity_func_calls]))
    price_list = list(chain.from_iterable(chain(result)))
    availiable_items = price_list
    # for is_avail, item_price in zip(availiability_list, price_list):
    #     if is_avail is True:
    #         availiable_items.append(item_price)

    # Sorting  based on item price
    availiable_items = sorted(availiable_items, key=lambda x: (x.selling_price, int(x.discount)))
    availiable_items = availiable_items[:top_k]
    result = [item.item_id for item in availiable_items]
    # TODO: Implementation goes here
    print(f' Please implement me')
    print(result)
    return result


if __name__ == '__main__':
    top_k = 10
    items = [str(i) for i in range(1000)]
    asyncio.run(return_top_cheapest_items(items, top_k))

# TODO
# Handle exceptions. - 3
# Replace some python functions with functions built from scratch - 4
# make return_top_cheapest_items sync - 1
# directly assign results - 2
# See if we can call availiable function first and then call price function only on availiable items
# Compare times of both of the above approaches