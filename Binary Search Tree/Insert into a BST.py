# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root):
            if root is None:
                return TreeNode(val)
            else:
                if root.val==val:
                    return root
                if root.val>val:
                    root.left=insert(root.left)
                else:
                    root.right=insert(root.right)
            return root
        return insert(root)
        '''Iterative
        node=TreeNode(val)
        if root==None:
            root=node
            return root
        prev=None
        temp=root
        while temp:
            if temp.val>val:
                prev=temp
                temp=temp.left
            elif temp.val<val:
                prev=temp
                temp=temp.right
        if prev.val>val:
            prev.left=node
        else:
            prev.right=node
        return root'''
        
