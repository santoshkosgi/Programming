class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n, start=1):
        output = []

        if start > n:
            return [None]

        for root_node in range(start, n + 1):
            left = self.generateTrees(start=start, n=root_node - 1)
            right = self.generateTrees(start=root_node + 1, n=n)
            for left_node in left:
                for right_node in right:
                    root = TreeNode(root_node)
                    root.left = left_node
                    root.right = right_node
                    output.append(root)
        return output

sol = Solution()
sol.generateTrees(3)