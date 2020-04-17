"""
LRU implementation using maxheap + dictionary

Assuming priority is an integer but can be easily changed to inert timestamp.
"""


class MaxHeap(object):
    """
    This class has methods which implement minheap, that are used by LRU
    """

    def __init__(self, memory_pages):
        self.heap = memory_pages

    def heapify(self, position):
        """
        This method assumes both left and right subtrees are min heaps and tries to place the
        root element in the right position.
        This function heapifies the heap at position. Assuming that both left and right children are already heaps.
        """
        start_index = position
        while True:
            left_child = 2 * start_index + 1
            right_child = 2 * start_index + 2
            if left_child < len(self.heap):
                if right_child < len(self.heap):
                    # If right child is present
                    if self.heap[right_child].priority < self.heap[left_child].priority and \
                            self.heap[right_child].priority < self.heap[start_index].priority:
                        self.heap[start_index], self.heap[right_child] = self.heap[right_child], self.heap[start_index]
                        self.heap[start_index].index = start_index
                        self.heap[right_child].index = right_child
                        start_index = right_child

                    elif self.heap[left_child].priority < self.heap[start_index].priority:
                        self.heap[start_index], self.heap[left_child] = self.heap[left_child], self.heap[start_index]
                        self.heap[start_index].index = start_index
                        self.heap[left_child].index = left_child
                        start_index = left_child
                    else:
                        break
                else:
                    if self.heap[left_child].priority < self.heap[start_index].priority:
                        self.heap[start_index], self.heap[left_child] = self.heap[left_child], self.heap[start_index]
                        self.heap[start_index].index = start_index
                        self.heap[left_child].index = left_child

                        start_index = left_child
                    else:
                        break
            else:
                # Its a leaf
                break

    def build_heap(self):
        n = int((len(self.heap) / 2) - 1)

        while n >= 0:
            self.heapify(n)
            n -= 1

    def delete_minelement(self):
        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heapify(0)
        self.heap = self.heap[0:-1]

class MemoryPage(object):
    """
    This class has methods and attributes related to a memory page.
    List of these memory pages objects are used to make a Minheap.
    """
    def __init__(self, page_name, priority=None):
        """
        page_name: name of the page. currently, this is a number.
        """
        self.page_name = page_name
        self.priority = priority
        self.index = None

page_sequence = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
memory_pages = [MemoryPage(i, index) for index, i in enumerate(page_sequence[:4])]
memory_pages_dict = {i: memory_pages[index] for index, i in enumerate(page_sequence[:4])}
from random import shuffle
shuffle(memory_pages)
for index, _ in enumerate(memory_pages):
    memory_pages[index].index = index
maxheap = MaxHeap(memory_pages)
print([(maxheap.heap[i].page_name, maxheap.heap[i].priority, maxheap.heap[i].index) for i in range(len(maxheap.heap))])
maxheap.build_heap()
print([(maxheap.heap[i].page_name, maxheap.heap[i].priority, maxheap.heap[i].index) for i in range(len(maxheap.heap))])

max_priority = 3

for page_number in page_sequence[4:]:
    # Page is already cached
    print(page_number)
    if page_number in memory_pages_dict:
        print("page already found, so updating the priority", page_number)
        max_priority += 1
        memory_pages_dict[page_number].priority = max_priority
        maxheap.heapify(memory_pages_dict[page_number].index)
        print([(maxheap.heap[i].page_name, maxheap.heap[i].priority, maxheap.heap[i].index) for i in range(len(maxheap.heap))])
    else:
        print("page not found", page_number)
        memory_pages_dict.pop(maxheap.heap[0].page_name, None)
        maxheap.delete_minelement()
        max_priority += 1
        new_page = MemoryPage(page_number, max_priority)
        new_page.index = len(maxheap.heap)
        maxheap.heap.append(new_page)
        memory_pages_dict[page_number] = new_page
        print([(maxheap.heap[i].page_name, maxheap.heap[i].priority, maxheap.heap[i].index) for i in range(len(maxheap.heap))])
