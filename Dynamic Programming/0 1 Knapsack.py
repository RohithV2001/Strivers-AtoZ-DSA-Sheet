from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def knapsack(id,wt,val,n,W,dp):
    if id==0:
        if wt[0]<=W:
            return val[0]
        return 0
    if dp[id][W]!=-1:
        return dp[id][W]
    notTaken=0+knapsack(id-1,wt,val,n,W,dp)
    taken=-9999
    if wt[id]<=W:
        taken=val[id]+knapsack(id-1,wt,val,n,W-wt[id],dp)
    dp[id][W]=max(taken,notTaken)
    return dp[id][W]

T=int(input())
for _ in range(T):
    n=int(input())
    wt=list(map(int,input().split()))
    val=list(map(int,input().split()))
    W=int(input())
    dp=[[-1 for i in range(W+1)] for j in range(n)]
    print(knapsack(n-1,wt,val,n,W,dp))
