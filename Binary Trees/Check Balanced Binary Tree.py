class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            l=dfs(root.left)
            if l==-1:
                return -1
            r=dfs(root.right)
            if r==-1:
                return -1
            if abs(l-r)>1:
                return -1
            else:
                return 1+max(l,r)
        if root is None:
            return True
        return dfs(root)!=-1
