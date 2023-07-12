class Solution:    
    def printNos(self,N):
        if N==0:
            return 
        else:
            self.printNos(N-1)
            print(N,'',end='')
