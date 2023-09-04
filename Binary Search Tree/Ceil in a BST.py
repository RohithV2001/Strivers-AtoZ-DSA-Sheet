class Solution:
    def findCeil(self,root, inp):
        ceil=-1
        while root:
            if root.key==inp:
                ceil=inp
                break
            elif root.key<inp:
                root=root.right
            else:
                ceil=root.key
                root=root.left
        return ceil
