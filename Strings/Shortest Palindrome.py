class Solution:
    def shortestPalindrome(self, s: str) -> str:
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
        temp=s+"#"+s[::-1]
        m=len(temp)
        ans=calculate(temp,m)
        mp=len(s)-ans[len(ans)-1]
        return s[-mp:][::-1]+s if mp>0 else s
