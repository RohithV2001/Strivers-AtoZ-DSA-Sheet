class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N):
                if j==0 or j==N-1 or i==0 or i==N-1:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
