class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            if node==None:
                return node
            if node.next==None:
                return node
            node1=reverse(node.next)
            node.next.next=node
            node.next=None
            return node1
        return reverse(head)
