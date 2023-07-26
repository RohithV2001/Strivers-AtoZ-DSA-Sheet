def constructDLL(arr: [int]) -> Node:
    head=Node(arr[0])
    temp=head
    for i in range(1,len(arr)):
        cnode=Node(arr[i])
        temp.next=cnode
        cnode.prev=temp
        temp=temp.next
    return head
