class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        l=0
        mx=0
        cl=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            cl=r-l+1
            if cl-max(freq.values())<=k:
                mx=max(mx,cl)
            else:
                freq[s[l]]-=1
                l+=1
        return mx
