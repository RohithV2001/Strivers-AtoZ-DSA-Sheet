class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        stack=[]
        res=[]
        node=root
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                res.append(node.val)
                node=node.right
        return res
