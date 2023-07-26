def insertAtTail(head: Node, k: int) -> Node:
    last=head
    n_node=Node(k)
    n_node.next=None
    if head is None:
        n_node.prev=None
        head=n_node
        return head
    while last.next:
        last=last.next
    last.next=n_node
    n_node.prev=last
    return head
