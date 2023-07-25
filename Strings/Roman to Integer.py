class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        c=0
        p=0
        for i in s[::-1]:
            if d[i]>=p:
                c=c+d[i]
            else:
                c=c-d[i]
            p=d[i]
        return c
