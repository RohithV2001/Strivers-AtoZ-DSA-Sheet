def lengthOfLoop(head: Node) -> int:
    if head is None:
        return 0
    slow=head
    fast=head
    flag=0
    while slow and slow.next and fast and fast.next and fast.next.next:
        if slow==fast and flag!=0:
            slow=slow.next
            c=1
            while slow!=fast:
                slow=slow.next
                c+=1
            return c
        slow=slow.next
        fast=fast.next.next
        flag=1
    return 0
