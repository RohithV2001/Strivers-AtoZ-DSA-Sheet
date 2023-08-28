class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxpath(root):
            if not root:
                return 0
            lt=max(0,maxpath(root.left))
            rt=max(0,maxpath(root.right))
            self.maxi=max(self.maxi,lt+rt+root.val)
            return max(lt,rt)+root.val
        self.maxi=-9999
        maxpath(root)
        return self.maxi
