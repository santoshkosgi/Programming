# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        first_column = [(row.val, index, row) for index, row in enumerate(lists)]
        heap = Heap(first_column)
        heap.build_heap()
        result = None
        last_node = None
        while True:
            top_node = heap.pop_top_element()
            number, row_num, row = top_node
            node = ListNode(number)
            if result is None:
                result = node
                last_node = node
            else:
                last_node.next = node
                last_node = last_node.next
            if row.next is not None:
                row = row.next
                heap.add_node((row.val, row_num, row))
            if len(heap.heap) == 0:
                break
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
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = ListNode(2)
list3.next = ListNode(6)
sol.mergeKLists([list1, list2, list3])