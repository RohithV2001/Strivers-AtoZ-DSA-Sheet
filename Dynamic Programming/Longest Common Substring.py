import sys
def lcs(str1: str, str2: str) -> int:
    result=-sys.maxsize
    m=len(str1)
    n=len(str2)
    dp=[[0 for _ in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                result=max(result,dp[i][j])
    return result
