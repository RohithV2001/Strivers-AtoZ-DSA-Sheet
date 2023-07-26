class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last=None
        cur=head
        while cur:
            nn=cur.next
            cur.next=last
            last=cur
            cur=nn
        return last
