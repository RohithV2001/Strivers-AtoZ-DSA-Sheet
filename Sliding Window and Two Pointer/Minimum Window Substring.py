class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini=len(s)+1
        i=0
        start=0
        end=0
        cnt=len(t)
        d=dict()
        for c in t:
            d[c]=d.get(c,0)+1
        while end<len(s):
            if s[end] in d:
                if d[s[end]]>0:
                    cnt-=1
                d[s[end]]-=1
            end+=1
            while cnt==0:
                if end-start<mini:
                    mini=end-start
                    i=start
                if s[start] in d:
                    d[s[start]]+=1
                    if d[s[start]]>0:
                        cnt+=1
                start+=1
        if mini==len(s)+1:
            return ''
        return s[i:i+mini]
