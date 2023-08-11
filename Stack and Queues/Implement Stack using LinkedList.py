class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    
    def empty(self):
        return self.head==None
        
    def push(self,num):
        if self.head==None:
            self.head=Node(num)
        else:
            newnode=Node(num)
            newnode.next=self.head
            self.head=newnode
        
        
    def pop(self):
        if self.empty():
            return None
        else:
            ele=self.head
            self.head=self.head.next
            ele.next=None
            return ele.data
            
    def peek(self):
        if self.empty():
            return None
        else:
            return self.head.data
            
    def display(self):
        temp=self.head
        if self.empty():
            print("Error")
        else:
            while temp:
                print(temp.data, end=" ")
                temp=temp.next
                
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print()
print("Top Element",s.peek())
print()
s.pop()
s.pop()
s.display()
