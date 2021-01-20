# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        end = None
        while (l1 is not None) and (l2 is not None):
            if l1.val >= l2.val:
                if result is None:
                    result = l2
                    l2 = l2.next
                    result.next = None
                    end = result
                else:
                    end.next = l2
                    l2 = l2.next
                    end = end.next
                    end.next = None
            else:
                if result is None:
                    result = l1
                    l1 = l1.next
                    result.next = None
                    end = result
                else:
                    end.next = l1
                    l1 = l1.next
                    end = end.next
                    end.next = None

        if l1 is not None:
            if result is None:
                result = l1
            else:
                end.next = l1
        if l2 is not None:
            if result is None:
                result = l2
            else:
                end.next = l2
        return result

sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

sol.mergeTwoLists(l1, l2)