class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummyA, dummyB = headA, headB 
        while dummyA != dummyB:
            dummyA = headB if dummyA is None else dummyA.next 
            dummyB = headA if dummyB is None else dummyB.next
        return dummyA 
