# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx,val in enumerate(inorder)}
        preorder_index = 0
        def helper(left,right)->Optional[TreeNode]:
            nonlocal preorder_index
            if left>right:
                return None
            node_val = preorder[preorder_index]
            node = TreeNode(node_val)
            preorder_index+=1
            mid = inorder_map[node_val]
            node.left = helper(left,mid-1)
            node.right = helper(mid+1,right)
            return node
        return helper(0,len(inorder)-1)