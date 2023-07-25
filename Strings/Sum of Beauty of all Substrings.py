class Solution:
    def beautySum(self, s: str) -> int:
        '''Using List'''
        r=0
        for i in range(len(s)):
            c=[0]*27
            for j in range(i,len(s)):
                c[ord(s[j])-97]+=1
                r += max(c) - min(x for x in c if x)
        return r
        '''Using HashMap'''
        beauty=0
        for i in range(len(s)-2):
            Freq={}
            for j in range(i,len(s)):
                Freq.setdefault(s[j],0)
                Freq[s[j]]+=1
                beauty+=max(Freq.values())-min(Freq.values())
        return beauty
