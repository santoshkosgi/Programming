def quicksort(array, start_index, end_index):
    """
    @param array: An array which needs to be sorted.
    @param start_index: Start index of the subarray that needs to be considered
    @param end_index: End index of the subarray that needs to be considered
    @return: Sorted array between start and end index
    """
    low = start_index
    high = end_index - 1
    pivot = array[end_index]
    if not (low <= high):
        return
    while low <= high:
        while array[low] <= pivot and low < end_index:
            low += 1
        while array[high] > pivot and high > start_index:
            high -= 1
        if low < high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[low], array[end_index] = array[end_index], array[low]
    quicksort(array, start_index, low-1)
    quicksort(array, low+1, end_index)


if __name__ == '__main__':
    array = [7,5,6,4,3,1]
    quicksort(array=array, start_index=0, end_index=len(array) -1 )
    print(array)

