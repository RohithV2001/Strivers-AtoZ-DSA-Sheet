# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        def kthsmall(root):
            if root is None:
                return None
            left=kthsmall(root.left)
            if left!=None:
                return left
            self.k-=1
            if self.k==0:
                return root.val
            return kthsmall(root.right)
        return kthsmall(root)
        '''
        self.l=[]
        def preorder(root):
            if root is None:
                return None
            self.l.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        self.l.sort()
        if k<=len(self.l):
            return self.l[k-1]
        else:
            return -1
            '''
        
