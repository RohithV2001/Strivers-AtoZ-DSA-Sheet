from typing import List

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def createTree(arr: List[int]) -> Node:
    root=Node(arr[0])
    root.left=Node(arr[1])
    root.right=Node(arr[2])
    root.left.left=Node(arr[3])
    root.left.right=Node(arr[4])
    root.right.left=Node(arr[5])
    root.right.right=Node(arr[6])
    return root
