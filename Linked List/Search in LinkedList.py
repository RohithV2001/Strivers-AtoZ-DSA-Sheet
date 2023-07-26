def searchInLinkedList(head, k):
    temp=head
    while temp:
        if temp.data==k:
            return 1
        temp=temp.next
    return 0
