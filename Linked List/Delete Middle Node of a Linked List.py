class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp=head
        if temp and temp.next:
            while temp.next!=slow:
                temp=temp.next
            temp.next=temp.next.next
        return head
