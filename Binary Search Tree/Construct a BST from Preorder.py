# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i=0
        def helper(bound):
            if self.i==len(preorder) or preorder[self.i]>bound:
                return None
            root=TreeNode(preorder[self.i])
            self.i+=1
            root.left=helper(root.val)
            root.right=helper(bound)
            return root
        return helper(float('inf'))

        '''
        return self.helper(preorder[::-1],float('inf'))
    def helper(self,A,b):
        if not A or A[-1]>b:
            return None
        root=TreeNode(A.pop())
        root.left = self.helper(A, root.val)
        root.right = self.helper(A, b)
        return root'''
