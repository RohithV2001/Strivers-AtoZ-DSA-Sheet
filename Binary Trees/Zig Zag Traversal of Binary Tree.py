# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cl=[]
        res=[]
        if root!=None:
            cl.append(root)
        lr=True
        while len(cl)>0:
            nl=[]
            llr=[]
            while len(cl)>0:
                node=cl.pop()
                llr.append(node.val)
                if lr:
                    if node.left!=None:
                        nl.append(node.left)
                    if node.right!=None:
                        nl.append(node.right)
                else:
                    if node.right!=None:
                        nl.append(node.right)
                    if node.left!=None:
                        nl.append(node.left)
            cl=nl
            res.append(llr)
            lr=not lr
        return res
