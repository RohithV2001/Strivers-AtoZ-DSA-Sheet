class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic=dict()
        self.head=ListNode(0,0)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node=self.dic[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node=self.dic[key]
            self.remove(node)
            self.insert(node)
            node.value=value
        else:
            if len(self.dic)==self.capacity:
                del self.dic[self.tail.prev.key]
                self.remove(self.tail.prev)
            node=ListNode(key,value)
            self.dic[key]=node
            self.insert(node)
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def insert(self,node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
