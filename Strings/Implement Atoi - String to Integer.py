class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        sign=1
        if s[0]=='-':
            sign=-1
        if s[0]=='-' or s[0]=='+':
            s=s[1:]
        n=0
        for i in s:
            if i in '0123456789':
                n=n*10+int(i)
            else:
                break
        n=sign*n
        if n>=2**31:
            return 2**31-1
        if n<=-2**31:
            return -2**31
        return n
