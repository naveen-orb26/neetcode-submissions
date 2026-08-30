# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdia = 0
        def dfs(node):
            nonlocal maxdia
            if not node:
                return 0
            lefth = dfs(node.left)
            righth = dfs(node.right)
            dia = max(lefth,righth)
            maxdia = max(maxdia,lefth+righth)
            return 1+dia
        dfs(root)
        return maxdia