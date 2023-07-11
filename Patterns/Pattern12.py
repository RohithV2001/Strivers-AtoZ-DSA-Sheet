class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j,'',end='')
            for k in range((2*N)-(2*i)):
                print('  ',end='')
            for l in range(i,0,-1):
                print(l,'',end='')
            print()
