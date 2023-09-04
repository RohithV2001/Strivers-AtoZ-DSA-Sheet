# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        """
        self.first=None
        self.middle=None
        self.last=None
        self.prev=TreeNode(float('-inf'))
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev!=None and root.val<self.prev.val:
                if self.first==None:
                    self.first=self.prev
                    self.middle=root
                else:
                    self.last=root
            self.prev=root
            inorder(root.right)
        inorder(root)
        if self.first!=None and self.last!=None:
            self.first.val,self.last.val=self.last.val,self.first.val
        elif self.first!=None and self.middle!=None:
            self.first.val,self.middle.val=self.middle.val,self.first.val
        
        '''
        self.l=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.l.append(root.val)
            inorder(root.right)
        inorder(root)
        self.l.sort()
        self.i=0
        def inorderswap(root):
            if not root:
                return
            inorderswap(root.left)
            if self.l[self.i]!=root.val:
                root.val=self.l[self.i]
            self.i+=1
            inorderswap(root.right)
        inorderswap(root)
        
        '''
