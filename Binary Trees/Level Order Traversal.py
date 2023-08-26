class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 
        l=[]
        d={}
        p=[]
        l.append([root,1])
        node=None
        while l:
            node,depth=l.pop(0)
            if depth not in d:
                d[depth]=[node.val]
            else:
                d[depth].append(node.val)
            if node.left is not None:
                l.append([node.left,depth+1])
            if node.right is not None:
                l.append([node.right,depth+1])
        for i in sorted(d.keys()):
            p.append(d[i])
        return p
