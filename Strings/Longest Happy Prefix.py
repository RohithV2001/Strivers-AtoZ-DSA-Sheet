class Solution:
    def longestPrefix(self, s: str) -> str:
        def calculate(pattern,m):
            lps=[0]*m
            lps[0]=0
            i=1
            len=0
            while i<m:
                if pattern[i]==pattern[len]:
                    len+=1
                    lps[i]=len
                    i+=1
                else:
                    if len!=0:
                        len=lps[len-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        m=len(s)
        ans=calculate(s,m)
        res=ans[m-1]
        if res==0:
            return ""
        else:
            return s[:res]
