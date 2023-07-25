class Solution:
    def maxDepth(self, s: str) -> int:
        mx=0
        c=0
        opened=0
        for i in s:
            if i =='(':
                c+=1
                if c>mx:
                    mx=c
            elif i==')':
                c-=1
        if c==0:
            return mx
