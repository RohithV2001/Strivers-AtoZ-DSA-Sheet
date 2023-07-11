class Solution:
    def printTriangle(self, N):
        for i in range((2*N)-1):
            for j in range((2*N)-1):
                top=i
                left=j
                right=((2*N)-2)-j
                down=((2*N)-2)-i
                print((N-min(min(top,down),min(left,right))),'',end='')
            print()
