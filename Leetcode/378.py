class Solution:
    def kthSmallest(self, matrix, k):
        """
        This problem can be solved using min-heaps and Binary Search.
        Here I will try to solve using both.
        Min-Heap: The idea is to maintain a heap of size = n(number of rows of matrix).
        Insert the first column of the matrix to the heap, store the information of the column along
        with the number. Now, pop the minimum element of the heap, based on the row of the element
        popped, insert the next element into the heap. Do this till k times.
        To insert an element into heap it takes log(k) time so the complexity is n * log(k)

        Binary Search: number at the first row forst column is the smallest number of the matrix
        number at the last row and last column is the largest number of the matrix. Now, we have to
        do a binary search between this smallest and largest number for the required number.
        We have to find which row this middle element can be present by doing binary search on the first
        column of the matrix, then by performing binary search on this resultant row, we can
        come up with the closest number.  ????
        """
        first_column = [(row[0], index, 0) for index, row in enumerate(matrix)]
        heap = Heap(first_column)
        heap.build_heap()
        for _ in range(k):
            top_node = heap.pop_top_element()
            number, row_num, column_num = top_node
            if column_num+1 <= len(matrix) - 1:
                heap.add_node((matrix[row_num][column_num+1], row_num, column_num + 1))
        return number

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
matrix = [[1,2],[3,3]]
print(sol.kthSmallest(matrix, 2))