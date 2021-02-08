class Solution:
    def topKFrequent(self, nums, k: int):
        """
        The idea is to find the frequency of each of the number and use min-heap to do this.
        """

        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1

        """
        Now the idea is to maintain a min-heap of size k and if the heap is full and freq of new
        number is less than top of min heap, dont insert it... else insert it.
        """
        array = []
        heap_built = False
        for num, frequency in freq_dict.items():
            if len(array) < k:
                array.append((frequency, num))
            if heap_built is False and len(array) == k:
                heap = Heap(array)
                heap.build_heap()
                heap_built = True
                continue
            if len(array) == k and frequency > heap.heap[0][0]:
                heap.pop_top_element()
                heap.add_node((frequency, num))

        result = [None] * k

        index = k - 1
        while index >= 0:
            freq, num = heap.pop_top_element()
            result[index] = num
            index -= 1
        return result


class Heap:
    """
    Min Heap
    """

    def __init__(self, array):
        self.array = array
        self.heap = array

    def heapify(self, number):
        """
        This function adds an element into the heap.
        Each node of heap contains a tuple of (number, row_number)
        Idea is to insert new number at the last of the heap and traverse it to the top.
        Till the heap property is not voilated.
        """
        self.heap.append(number)
        curr_index = len(self.heap) - 1
        parent_index = self.get_parent_index(curr_index)
        while curr_index > parent_index and self.heap[parent_index][0] > self.heap[curr_index][0]:
            # Swap elements at parent and child indices
            self.heap[parent_index], self.heap[curr_index] = self.heap[curr_index], self.heap[parent_index]
            curr_index = parent_index
            parent_index = self.get_parent_index(curr_index)

    def heapify_top_down(self, position):
        """
        This function assumes that both left and right child of this position are min-heaps already
        and tries to make min-heap which is rooted at this position.
        """
        start_index = position
        while True:
            left_child = 2 * start_index + 1
            right_child = 2 * start_index + 2
            if left_child < len(self.heap):
                if right_child < len(self.heap):
                    # If right child is present
                    if self.heap[right_child][0] < self.heap[left_child][0] and \
                            self.heap[right_child][0] < self.heap[start_index][0]:
                        self.heap[start_index], self.heap[right_child] = self.heap[right_child], self.heap[start_index]
                        start_index = right_child

                    elif self.heap[left_child][0] < self.heap[start_index][0]:
                        self.heap[start_index], self.heap[left_child] = self.heap[left_child], self.heap[start_index]
                        start_index = left_child
                    else:
                        break
                else:
                    if self.heap[left_child][0] < self.heap[start_index][0]:
                        self.heap[start_index], self.heap[left_child] = self.heap[left_child], self.heap[start_index]
                        start_index = left_child
                    else:
                        break
            else:
                # Its a leaf
                break

    def build_heap(self):
        """
        This function inserts the elements to the heap by calling heapify function.
        """
        n = int((len(self.array) / 2) - 1)

        while n >= 0:
            self.heapify_top_down(n)
            n -= 1

    def pop_top_element(self):
        top_node = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap = self.heap[0:len(self.heap) - 1]
        if len(self.heap) > 0:
            self.heapify_top_down(0)
        return top_node

    def add_node(self, num_tup):
        self.heapify(num_tup)

    @staticmethod
    def get_parent_index(index):
        """
        If the index is even, parent index is index/2 - 1
        else floor of index/2
        """
        if index == 0:
            return 0
        if index % 2 == 0:
            return int(index / 2 - 1)
        return int(index / 2)


sol = Solution()
sol.topKFrequent([1,1,1,2,2,3], 2)