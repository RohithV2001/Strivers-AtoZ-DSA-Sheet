def merge(a,b):
    temp=Node(0)
    res=temp
    while a is not None and b is not None:
        if a.data<b.data:
            temp.child=a
            temp=temp.child
            a=a.child
        else:
            temp.child=b
            temp=temp.child
            b=b.child
    if a:
        temp.child=a
    if b:
        temp.child=b 
    return res.child 


def flattenLinkedList(head: Node) -> Node:
    if head is None or head.next is None:
        return head 
    head.next=flattenLinkedList(head.next)
    head=merge(head,head.next)
    return head 
