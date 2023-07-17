class Solution(object):
    def generate(self, numRows):
        l=[[]]*numRows
        for i in range(1,numRows):
            l[i]=[1]*(i+1)
        l[0]=[1]
        if numRows==1:
            return l
        elif numRows==2:
            return l
        else:
            for i in range(2,numRows):
                for j in range(1,len(l[i])-1):
                    l[i][j]=l[i-1][j-1]+l[i-1][j]
            return l
