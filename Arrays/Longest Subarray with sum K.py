def longestSubarrayWithSumK(a: [int], k: int) -> int:
    l=0
    r=0
    s=a[0]
    mx=0
    while r<len(a):
        while l<=r and s>k:
            s-=a[l]
            l+=1
        if s==k:
            mx=max(mx,r-l+1)
        r+=1
        if r<len(a):
            s+=a[r]
    return mx
