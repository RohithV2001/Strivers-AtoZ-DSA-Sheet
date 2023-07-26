class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        d=ListNode(None)
        d.next=head
        while d.next:
            l+=1
            d=d.next
        if l==n:
            return head.next
        res=ListNode(None)
        res.next=head
        c=0
        while c<l-1-n:
            head=head.next
            c+=1
        head.next=head.next.next
        return res.next
