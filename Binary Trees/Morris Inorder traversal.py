class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        cur=root
        while cur:
            if cur.left==None:
                l.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                if prev.right==None:
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right=None
                    l.append(cur.val)
                    cur=cur.right
        return l
