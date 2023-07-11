class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            for j in range(i,0,-1):
                print('*',end=' ')
            print()
