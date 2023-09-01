# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''O(logN) Approach'''
        def lefth(cur):
            h=0
            while cur!=None:
                h+=1
                cur=cur.left
            return h
        
        def righth(cur):
            h=0
            while cur!=None:
                h+=1
                cur=cur.right
            return h

        def nodes(node):
            if node is None:
                return 0
            lh=lefth(node)
            rh=righth(node)
            if lh==rh:
                return (2**lh)-1
            lnodes=nodes(node.left)
            rnodes=nodes(node.right)
            return lnodes+rnodes+1
        return nodes(root)
        '''
        O(n) Approach
        self.c=0
        def order(root):
            if not root:
                return
            self.c+=1
            order(root.left)
            order(root.right)
        order(root)
        return self.c
        '''
