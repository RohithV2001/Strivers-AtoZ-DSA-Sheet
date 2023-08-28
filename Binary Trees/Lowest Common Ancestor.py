# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root,p,q):
            
            if root==None or root==p or root==q:
                return root
            l=lca(root.left,p,q)
            r=lca(root.right,p,q)
            if l==None:
                return r
            elif r==None:
                return l
            else:
                return root
        return lca(root,p,q)
