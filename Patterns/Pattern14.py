class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print(chr(65+j),end='')
            print()
