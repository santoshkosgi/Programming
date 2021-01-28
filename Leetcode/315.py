class Node(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.solution = 0
        self.left = None
        self.right = None
        self.num_of_elements_in_left_subtree = 0


class Solution:

    def countSmaller(self, nums):
        """
        The idea is to process the array from right.
        At every point store index and number of the array in stack.
        When pushing the element to array, push if top element of the array is less than the number,
        if not keep on popping the stack. When stack is empty insert it. Before inserting the element
        into the stack, populate countSmaller[] with the size of the stack.
        """
        """
        Above idea did not cover all the cases. Trying out BST. Will process the array from right to left and 
        at every node we will store the number of elements that are in left subtree of this node and 
        req.answer and also the index of the element in the actual array. Later we will do some traversal
        of the BST to populate the required solution array
        """
        index = len(nums) - 1

        root = None

        solution = [0 for _ in nums]

        while index >= 0:
            if root is None:
                root = Node(nums[index], index)
            else:
                req_pos = root
                parent = root
                node = Node(nums[index], index)
                while req_pos is not None:
                    if nums[index] <= req_pos.value:
                        req_pos.num_of_elements_in_left_subtree += 1
                        parent = req_pos
                        req_pos = req_pos.left
                    else:
                        node.solution = node.solution + req_pos.num_of_elements_in_left_subtree + 1
                        solution[index] = node.solution
                        parent = req_pos
                        req_pos = req_pos.right
                if nums[index] <= parent.value:
                    parent.left = node
                else:
                    parent.right = node

            index -= 1

        return solution


sol = Solution()
print(sol.countSmaller([5,2,6,1]))