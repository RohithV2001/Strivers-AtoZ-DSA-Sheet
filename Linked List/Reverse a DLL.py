def reverseDLL(head):
    temp=None
    cur=head
    while cur:
        temp=cur.prev
        cur.prev=cur.next
        cur.next=temp
        cur=cur.prev
    if temp:
        head=temp.prev

    return head
