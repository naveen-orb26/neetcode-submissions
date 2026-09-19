# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node,maxsofar):
            if not node:
                return 0
            if node.val>=maxsofar:
                maxsofar = node.val
                count = 1
            else:
                count = 0
            return count+dfs(node.left,maxsofar)+dfs(node.right,maxsofar)
        
        return dfs(root,root.val)
            
