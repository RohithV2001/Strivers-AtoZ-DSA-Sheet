def reverse(head):
    prev=None
    while head:
        Next=head.next
        head.next=prev
        prev=head
        head=Next
    return prev


def addOne(head: Node) -> Node:
    head=reverse(head)
    curr=head
    carry=1
    while curr:
        curr.data+=carry
        carry=curr.data//10
        curr.data%=10
        
        if not carry:
            break
        
        curr=curr.next
    
    
    head=reverse(head)
    if carry:
        newNode=Node(1)
        newNode.next=head
        head=newNode
    return head
