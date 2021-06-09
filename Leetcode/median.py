def get_median_array(array):
    median_array = []
    max_heap = Heap()
    min_heap = Heap()
    max_heap_elements = 0
    min_heap_elements = 0
    max_heap.insert(array[0])
    max_heap_elements += 1
    median_array.append(array[0])
    # 1,4,3,2,5,6
    for index in range(1, len(array)):
        if array[index] > max_heap[0]:
            if min_heap_elements == max_heap_elements or max_heap_elements > min_heap_elements:
                min_heap.insert(array[index])
                min_heap_elements += 1
                # Compute Median
                median_array.append(compute_median(max_heap, min_heap))
            else:
                if array[index] < min_heap[0]:
                    max_heap.insert(array[index])
                    max_heap_elements += 1
                    # Compute Median
                    median_array.append(compute_median(max_heap, min_heap))
                else:
                    min_element = min_heap.pop()
                    max_heap.insert(min_element)
                    min_heap.insert(array[index])
                    max_heap_elements += 1
                    # Compute Median
                    median_array.append(compute_median(max_heap, min_heap))
        else: # array[index] <= max_heap[0]
            if max_heap_elements == min_heap_elements or min_heap_elements > max_heap_elements:
                max_heap.insert(array[index])
                max_heap_elements += 1
                # Compute median
                median_array.append(compute_median(max_heap, min_heap))
            else:
                max_element = max_heap.pop()
                min_heap.insert(max_element)
                max_heap.insert(array[index])
                min_heap_elements += 1
                # Compute Median
                median_array.append(compute_median(max_heap, min_heap))
    return median_array

def compute_median(max_heap, min_heap):
    total_len = len(max_heap) + len(min_heap)
    if total_len % 2 == 0:
        return int((max_heap[0] + min_heap[0])/2)
    if len(max_heap) > len(min_heap):
        return max_heap[0]
    return min_heap[0]