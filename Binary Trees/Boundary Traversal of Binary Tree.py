#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        res=[]
        def isLeaf(node):
            return node.left==None and node.right==None
        
        def leftorder(node):
            cur=node.left
            while cur:
                if isLeaf(cur)==False:
                    res.append(cur.data)
                if cur.left!=None:
                    cur=cur.left
                else:
                    cur=cur.right
        
        def rightorder(node):
            temp=[]
            cur=node.right
            while cur:
                if isLeaf(cur)==False:
                    temp.append(cur.data)
                if cur.right!=None:
                    cur=cur.right
                else:
                    cur=cur.left
            for i in temp[::-1]:
                res.append(i)
        
        def bottom(node):
            if isLeaf(node)==True:
                res.append(node.data)
                return
            if node.left!=None:
                bottom(node.left)
            if node.right!=None:
                bottom(node.right)
        
        if isLeaf(root)==False:
            res.append(root.data)
        leftorder(root)
        bottom(root)
        rightorder(root)
        return res
            
        

