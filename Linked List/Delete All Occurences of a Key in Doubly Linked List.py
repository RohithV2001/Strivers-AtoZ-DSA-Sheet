def deleteAllOccurrences(head: Node, k: int) -> Node:
    while head and head.data == k:
        head = head.next
    
    cur = head

    while cur:
        if cur.data == k:
            pre = cur.prev
            nxt = cur.next
            pre.next = nxt
            cur = nxt
        else:
            cur = cur.next
    return head
