class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(i):
                print('*',end=' ')
            print()
