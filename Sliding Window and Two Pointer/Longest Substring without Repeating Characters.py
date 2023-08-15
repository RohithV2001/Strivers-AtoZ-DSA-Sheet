class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p=''
        l=0
        c=0
        for i in s:
            if i in p:
                p=p+i
                p=p[p.index(i)+1:]
                c=len(p)
            else:
                c=c+1
                p=p+i
                l=c if c>l else l
        return l
