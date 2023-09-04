class Solution:
    def floor(self, root, x):
        floor=-1
        while root:
            if root.data==x:
                floor=x
                break
            elif root.data<x:
                floor=root.data
                root=root.right
            else:
                root=root.left
        return floor
