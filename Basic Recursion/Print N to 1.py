class Solution:
    def printNos(self, n):
        if n==0:
            return 
        else:
            print(n,'',end='')
            self.printNos(n-1)
