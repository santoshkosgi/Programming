# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        root = head
        if head is None or head.next is None:
            return head
        prev_node = None
        last_distinct_element = None

        while root is not None:
            if prev_node is None:
                prev_node = root
                root = root.next
                continue
            if prev_node.val != root.val:
                last_distinct_element = prev_node
                break
            else:
                # We need to move to element which is not equal to prev_node.val
                while root is not None and root.val == prev_node.val:
                    root = root.next
                if root is None:
                    break
                prev_node = root
                root = root.next
                if root is None:
                    last_distinct_element = prev_node


        if last_distinct_element is None:
            return None
        if last_distinct_element.next is None:
            return last_distinct_element
        last_element = last_distinct_element
        head = last_distinct_element
        prev_node = head.next
        if prev_node.next is None:
            last_element.next = prev_node
            return last_distinct_element
        root = prev_node.next

        while root is not None:
            if prev_node is None:
                prev_node = root
                root = root.next
                continue
            if prev_node.val != root.val:
                last_element.next = prev_node
                last_element = last_element.next
                prev_node = root
                root = root.next
                if root is None:
                    last_element.next = prev_node
                    last_element = last_element.next
                continue
            if prev_node.val == root.val:
                while root is not None and root.val == prev_node.val:
                    root = root.next
                if root is None:
                    break
                prev_node = root
                root = root.next
                if root is None:
                    last_element.next = prev_node
                    last_element = last_element.next

        last_element.next = None
        return last_distinct_element

sol = Solution()
array = [1,2,3]
head = None
last = None
for num in array:
    if head is None:
        head = ListNode(num)
        last = head
    else:
        last.next = ListNode(num)
        last = last.next

sol.deleteDuplicates(head)