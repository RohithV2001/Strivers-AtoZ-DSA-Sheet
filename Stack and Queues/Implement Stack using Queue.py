from queue import Queue
class MyStack:

    def __init__(self):
        self.q=Queue()

    def push(self, x: int) -> None:
        n=self.q.qsize()
        self.q.put(x)
        for i in range(n):
            self.q.put(self.q.get())

    def pop(self) -> int:
        ele=self.q.get()
        return ele

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.qsize()==0
