class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        flag=0
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                flag=1
                break
        if flag==1:
            slow=head
            c=0
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        else:
            return None
