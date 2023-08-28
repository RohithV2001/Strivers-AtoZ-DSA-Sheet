class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        elif p==None and q==None:
            return True
        else:
            if p.val==q.val and self.isSameTree(p.left,q.left)==True and self.isSameTree(p.right,q.right)==True:
                return True
            else:
                return False
