class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(0,N-i-1):
                print(' ',end='')
            for k in range(0,i+1):
                print(chr(65+k),end='')
            for l in range(i-1,-1,-1):
                print(chr(65+l),end='')
            print()
