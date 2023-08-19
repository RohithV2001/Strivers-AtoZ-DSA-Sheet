class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        head=ListNode(None)
        cur=head
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i))
                lists[i]=lists[i].next
        while h:
            val,i=heapq.heappop(h)
            cur.next=ListNode(val)
            cur=cur.next
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i))
                lists[i]=lists[i].next
        return head.next
