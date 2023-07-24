class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=''
        t=0
        for i in s:
            if i=='(' and t>0:
                res=res+i
            if i==')' and t>1:
                res=res+i
            if i=='(':
                t+=1
            else:
                t-=1
        return res
