class Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

root=Node(1)
root.left=Node(2)
root.left.right=Node(5)
root.right=Node(3)
l=[]
def btp(root,s,x):
    if  root is None:
        return False
    s.append(root.val)
    if root.val==x:
        return True
    if btp(root.left,s,x) or btp(root.right,s,x):
        return True
    s.remove(s[len(s)-1])
    return False
s=[]
btp(root,s,3)
print(s)
