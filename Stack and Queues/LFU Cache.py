class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.freq=1
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
        
    def insert(self,node):
        headnext=self.head.next
        headnext.prev=node
        self.head.next=node
        node.prev=self.head
        node.next=headnext
        self.size+=1
    
    def remove(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next
        self.size-=1
    
    def removeTail(self):
        tail = self.tail.prev
        self.remove(tail)
        return tail
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.freq=collections.defaultdict(DLL)
        self.minsize=0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            return self.UpdateCache(self.cache[key],key,self.cache[key].val)
        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.cache:
            self.UpdateCache(self.cache[key], key, value)
        else:
            if len(self.cache)==self.capacity:
                prevTail = self.freq[self.minsize].removeTail()
                del self.cache[prevTail.key]
            node=ListNode(key,value)
            self.freq[1].insert(node)
            self.minsize=1
            self.cache[key]=node
    def UpdateCache(self,node,key,value):
        node=self.cache[key]
        node.val=value
        pf=node.freq
        node.freq+=1
        self.freq[pf].remove(node)
        self.freq[node.freq].insert(node)
        if pf==self.minsize and self.freq[pf].size==0:
            self.minsize+=1
        return node.val
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
