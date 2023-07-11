class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(((2*N)-(2*i))//2):
                print('*',end='')
            for k in range((2*i)):
                print(' ',end='')
            for j in range(((2*N)-(2*i))//2):
                print('*',end='')
            print()
        for i in range(N-1,-1,-1):
            for j in range(N-i):
                print('*',end='')
            for k in range(2*i):
                print(' ',end='')
            for j in range(N-i):
                print('*',end='')
            print()
