class MinStack:

    def __init__(self):
        self.A=[]
        self.M=[]
    def push(self, val: int) -> None:
        self.A.append(val)
        M=self.M
        M.append(val if not M else min(M[-1],val))

    def pop(self) -> None:
        self.M.pop()
        self.A.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.M[-1]
