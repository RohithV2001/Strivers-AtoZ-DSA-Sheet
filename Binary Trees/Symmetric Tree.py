class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        a=root.left
        b=root.right
        def mirror(a,b):
            if a==None and b==None:
                return 1
            if a==None or b==None:
                return 0
            if a.val!=b.val:
                return 0
            else:
                return mirror(a.left,b.right) and mirror(a.right,b.left)
        
        return mirror(a,b
