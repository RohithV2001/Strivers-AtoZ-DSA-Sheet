from typing import *

def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    dp=[-1]*n
    dp[0]=0
    for i in range(1,n):
        steps=float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                jump=dp[i-j]+abs(heights[i]-heights[i-j])
                steps=min(steps,jump)
        dp[i]=steps
    return dp[n-1]
