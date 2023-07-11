class Solution:
    def printTriangle(self, N):
        k=1
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(k,'',end='')
                k=k+1
            print()
