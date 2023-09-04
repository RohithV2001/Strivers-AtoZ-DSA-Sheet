class Solution:
    def findPreSuc(self, root, pre, succ, key):
        temp=root
        while root!=None:
            if root.key<key:
                pre=root
                root=root.right
            else:
                root=root.left
        root=temp
        while root!=None:
            if root.key<key:
                root=root.right
            else:
                succ=root
                root=root.left
