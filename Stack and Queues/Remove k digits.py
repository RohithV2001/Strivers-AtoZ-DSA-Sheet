class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[]
        c=0
        for i in num:
            while s and s[-1]>i and k:
                s.pop()
                k-=1
            if s or i is not '0':
                s.append(i)
        if k:
            s=s[0:-k]
        return ''.join(s) or '0'
