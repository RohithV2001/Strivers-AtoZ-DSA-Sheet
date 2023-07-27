class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        else:
            temp=head
            l=1
            while temp.next:
                l+=1
                temp=temp.next
            k=k%l
            temp.next=head
            end=l-k
            while end!=0:
                temp=temp.next
                end=end-1
            head=temp.next
            temp.next=None
            return head
