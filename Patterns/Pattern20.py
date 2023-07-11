class Solution:
    def printTriangle(self, N):
        for i in range(N-1,-1,-1):
            for j in range(N-i):
                print('*',end='')
            for k in range(2*i):
                print(' ',end='')
            for j in range(N-i):
                print('*',end='')
            print()
        N=N-1
        for i in range(1,N+1):
            for j in range(N-i+1):
                print('*',end='')
            for k in range(2*i):
                print(' ',end='')
            for j in range(N-i+1):
                print('*',end='')
            print()
