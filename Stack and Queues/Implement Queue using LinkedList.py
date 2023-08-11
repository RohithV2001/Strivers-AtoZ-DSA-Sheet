class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def empty(self):
        return self.front==None
        
    def enqueue(self,num):
        temp=Node(num)
        if self.front==None:
            self.front=temp
            self.rear=temp
        else:
            self.rear.next=temp
            self.rear=temp 
        
        
    def dequeue(self):
        if self.empty():
            return None
        else:
            ele=self.front
            self.front=self.front.next
            
            
            
    def display(self):
        temp=self.front
        if self.empty():
            print("Queue is Empty")
        else:
            while temp:
                print(temp.data, end=" ")
                temp=temp.next
                
s=Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.display()
print()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.display()
