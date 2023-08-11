from queue import LifoQueue
class MyQueue:

    def __init__(self):
        self.q=LifoQueue()
        self.q1=LifoQueue()
    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        if self.q1.empty():
            while not self.q.empty():
                self.q1.put(self.q.get())
        x=self.q1.get()
        return x


    def peek(self) -> int:
        if self.q1.empty():
            while not self.q.empty():
                self.q1.put(self.q.get())
        return self.q1.queue[-1]

    def empty(self) -> bool:
        return self.q1.empty() and self.q.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
