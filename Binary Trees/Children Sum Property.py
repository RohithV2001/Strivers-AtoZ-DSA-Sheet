'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''
def isParentSum(root):
    lt=0
    rt=0
    if root is None or(root.left is None and root.right is None):
        return 1
    else:
        if root.left!=None:
            lt=root.left.data
        if root.right!=None:
            rt=root.right.data
        if root.data==lt+rt and ((isParentSum(root.left)) and (isParentSum(root.right))):
            return 1
        else:
            return 0
    '''
    def func(root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        lt=func(root.left)
        rt=func(root.right)
        if lt+rt==root.data:
            return root.data
        return 0
    return func(root)'''
