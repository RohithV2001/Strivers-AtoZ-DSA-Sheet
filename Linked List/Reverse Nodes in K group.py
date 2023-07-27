class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        d=ListNode(0)
        d.next=head
        pre=d
        while c>=k:
            cur=pre.next
            nex=cur.next
            for i in range(1,k):
                cur.next=nex.next
                nex.next=pre.next
                pre.next=nex
                nex=cur.next
            pre=cur
            c-=k
        return d.next
