# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")
        def dfs(node):
            nonlocal maxsum
            if not node:
                return 0
            leftgain = max(0,dfs(node.left))
            rightgain = max(0,dfs(node.right))
            currentmax = node.val+leftgain+rightgain
            maxsum = max(currentmax,maxsum)
            return node.val + max(rightgain,leftgain)
        dfs(root) 
        return maxsum