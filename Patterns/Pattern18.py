class Solution:
    def printTriangle(self, N):
        for i in range(N):
            k=N-1
            for j in range(i+1):
               print(chr(65+k),'',end='')
               k=k-1
            print()
    
