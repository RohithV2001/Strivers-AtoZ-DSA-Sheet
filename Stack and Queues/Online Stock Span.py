class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        stack=self.stack
        curp,curs=price,1
        while stack and stack[-1][0]<=curp:
            pp,ps=stack.pop()
            curs+=ps
        stack.append((curp,curs))
        return curs
