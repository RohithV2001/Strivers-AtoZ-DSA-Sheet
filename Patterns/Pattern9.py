class Solution:
    def printDiamond(self, N):
        for i in range(1,N+1):
            for j in range(1,N-i+1):
                print(' ',end='')
            for j in range(1,i+1):
                print('* ',end='')
            print()
        for i in range(N,0,-1):
            for j in range(1,N-i+1):
                print(' ',end='')
            for j in range(1,i+1):
                print('* ',end='')
            print()
