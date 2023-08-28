class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.l=[]
        def rv(root,c):
            if root is None:
                return
            if c==len(self.l):
                self.l.append(root.val)
            rv(root.right,c+1)
            rv(root.left,c+1)
        rv(root,0)
        return self.l
