# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root):
            if root is None:
                return None
            if root.val==key:
                return helper(root)
            temp=root
            while root:
                if root.val>key:
                    if root.left!=None and root.left.val==key:
                        root.left=helper(root.left)
                        break
                    else:
                        root=root.left
                else:
                    if root.right!=None and root.right.val==key:
                        root.right=helper(root.right)
                        break
                    else:
                        root=root.right
            return temp
        
        def helper(root):
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                rightchild=root.right
                lastright=findlastright(root.left)
                lastright.right=rightchild
                return root.left
        def findlastright(root):
            if root.right is None:
                return root
            else:
                return findlastright(root.right)
        return delete(root)


        
