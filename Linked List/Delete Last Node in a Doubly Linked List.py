def deleteLastNode(head: Node) -> Node:
    last=head
    if last.next is None:
        head=None
        return head
    while last.next.next:
        last=last.next
    last.next=None
    return head
