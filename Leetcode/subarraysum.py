def subarray_sum(array, b):
    i = 0
    j = 0
    if len(array) == 0:
        if b == 0:
            return True
        return False
    temp_sum = array[0]

    while i < len(array) and j < len(array):
        if j == len(array) - 1 and temp_sum < b:
            return False
        if temp_sum < b:
            j += 1
            temp_sum += array[j]
        elif temp_sum > b:
            temp_sum -= array[i]
            i += 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(subarray_sum([1,1,5,3], 3))






