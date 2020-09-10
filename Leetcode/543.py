# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            diameter = 0
        else:
            diameter = 0
            return 0
        if root.left is None and root.right is None:
            return 0

        _, diameter = self.max_depth(root, diameter)
        return diameter

    def max_depth(self, root, diameter):
        if root is None:
            return 0, 0
        if root.left is None and root.right is None:
            return 0, 0

        left_depth, diameter_left = self.max_depth(root.left, diameter)
        if root.left is not None:
            left_depth += 1

        right_depth, diameter_right = self.max_depth(root.right, diameter)
        if root.right is not None:
            right_depth += 1
        if left_depth > 0 and right_depth > 0:
            cur_diameter = left_depth + right_depth
        else:
            cur_diameter = left_depth if left_depth > 0 else right_depth
        diameter = max(diameter_left, diameter_right, cur_diameter)
        return max(left_depth, right_depth), diameter


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
print(sol.diameterOfBinaryTree(root))