class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def constructLL(arr: [int]) -> Node:
    head=Node(0)
    curr=head
    for i in arr:
        newNode=Node(i)
        curr.next=newNode
        curr=curr.next
    return head.next
