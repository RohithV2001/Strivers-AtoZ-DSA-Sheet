# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,minval,maxval):
            if root is None:
                return True
            if root.val<=minval or root.val>=maxval:
                return False
            return valid(root.left,minval,root.val) and valid(root.right,root.val,maxval)
        return valid(root,float('-inf'),float('inf'))
                
        
