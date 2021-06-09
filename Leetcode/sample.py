# A = [5, -2, 3 , 1, 2]
# b = 3



# 4, 3, 5, 8, 7

# 4, 4, 5, 8, 8
# 3, 3, 5, 7, 7

import datetime

def read_csv(file_location):
    file_ = open(file_location, "r")
    prev_date = None
    prev_balance = None
    for line in file_:
        if prev_date is None:
            _, _, date, _, bal = line.split(",")
            prev_date = date
            prev_balance = bal
        else:
            _, _, date, _, bal = line.split(",")
            if prev_date == date:
                prev_balance = bal
                continue
            else:
                # There is change in date
                print(prev_date, prev_balance)






def find_imp_element(array):
    prefix_array = [0 for _ in array]
    suffix_array = [0 for _ in array]
    max_num = None
    for index, num in enumerate(array):
        if max_num is None:
            prefix_array[index] = num
            max_num = num
        else:
            prefix_array[index] = max(max_num, num)
            max_num = max(max_num, num)
    last_index = len(array) - 1
    min_num = None
    while last_index >= 0:
        if min_num is None:
            suffix_array[last_index] = array[last_index]
            min_num = array[last_index]
            last_index -= 1
        else:
            min_num = min(min_num, array[last_index])
            suffix_array[last_index] = min_num
            last_index -= 1
    result = []
    for index in range(len(array)):
        if prefix_array[index] == suffix_array[index]:
            result.append(array[index])

    return result





def find_max_sum(array, b):
    i = 0
    j = b
    max_sum = None
    prev_sum = None
    while i < len(array):
        if max_sum is None:
            max_sum = sum(array[i:j])
            prev_sum = max_sum
            i += 1
            j = (j+1) % len(array)
        else:
            req_sum = prev_sum - array[i-1] + array[j - 1]
            max_sum = max(req_sum, max_sum)
            prev_sum = req_sum
            i += 1
            j = (j + 1) % len(array)
    return max_sum

if __name__ == '__main__':
    # A = [5, -2, 3 , 1, 2]
    # b = 3
    # print(find_max_sum(A, b))

    array = [4, 3, 5, 8, 7]
    print(find_imp_element(array))


