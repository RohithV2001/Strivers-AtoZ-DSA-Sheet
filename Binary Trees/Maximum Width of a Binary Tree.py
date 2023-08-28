# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx=0
        self.d={}
        def width(root,depth,position):
            if root is None:
                return
            if depth not in self.d:
                self.d[depth]=position
            self.mx=max(self.mx,position-self.d[depth]+1)
            width(root.left,depth+1,position*2)
            width(root.right,depth+1,(position*2)+1)
        width(root,0,0)
        return self.mx
