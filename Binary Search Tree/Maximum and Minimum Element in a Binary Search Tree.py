class Solution:
    def findMax(self,root):
        if root is None:
            return None
        while root.right!=None:
            root=root.right
        return root.data
    def findMin(self,root):
        if root is None:
            return None
        while root.left!=None:
            root=root.left
        return root.data
