class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        while temp:
            node=Node(temp.val)
            node.next=temp.next
            temp.next=node
            temp=temp.next.next
        t=head
        while t:
            if t.random is not None:
                t.next.random=t.random.next
            t=t.next.next
        d=Node(0)
        itr=head
        temp=d
        fast=Node(0)
        while itr:
            fast=itr.next.next
            temp.next=itr.next
            itr.next=fast
            temp=temp.next
            itr=fast
        return d.next

        '''Using Hashmap'''
        '''temp=head
        d={None:None}
        while temp:
            d[temp]=Node(temp.val)
            temp=temp.next
        cur=head
        while cur:
            node=d[cur]
            node.next=d[cur.next]
            node.random=d[cur.random]
            cur=cur.next
        return d[head]'''
