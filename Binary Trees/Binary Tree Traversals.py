from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder=[]
    preorder=[]
    postorder=[]
    def inordertrav(root):
        if not root:
            return 
        inordertrav(root.left)
        inorder.append(root.data)
        inordertrav(root.right)
    def preordertrav(root):
        if not root:
            return
        preorder.append(root.data)
        preordertrav(root.left)
        preordertrav(root.right)
    def postordertrav(root):
        if not root:
            return 
        postordertrav(root.left)
        postordertrav(root.right)
        postorder.append(root.data)
    inordertrav(root)
    preordertrav(root)
    postordertrav(root)
    return [inorder,preorder,postorder]
