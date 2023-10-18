from typing import List

def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
    dp=[1 for _ in range(n)]
    hash=[0 for _ in range(n)]
    for i in range(n):
        hash[i]=i
        for j in range(0,i):
            if arr[j]<arr[i] and 1+dp[j]>dp[i]:
                dp[i]=1+dp[j]
                hash[i]=j
    ans=-1
    li=-1
    for i in range(n):
        if dp[i]>ans:
            ans=dp[i]
            li=i
    temp=[]
    temp.append(arr[li])
    while hash[li]!=li:
        li=hash[li]
        temp.append(arr[li])
    return temp[::-1]  
