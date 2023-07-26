def removeDuplicates(head: Node) -> Node:
    if head==None:
        return None
    temp=head
    while temp:
        if (temp.next!=None) and (temp.data==temp.next.data) :
            nxt=temp.next.next
            temp.next=nxt
        else:
            temp=temp.next     
    return head
