class Stack:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.stack=[0]*self.capacity
        self.idx=0
        self.size=self.capacity
        

    def push(self, num: int) -> None:
        if self.idx==self.size:
            return -1
        self.stack[self.idx]=num
        self.idx=self.idx+1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.idx=self.idx-1
        return self.stack[self.idx]
    
    def top(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[self.idx-1]        
    
    def isEmpty(self) -> int:
        if self.idx==0:
            return 1
        else:
            return 0
        

    
    def isFull(self) -> int:
        if self.idx==self.size:
            return -1
        else:
            return 0
