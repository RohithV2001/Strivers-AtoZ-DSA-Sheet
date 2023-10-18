from os import *
from sys import *
from collections import *
from math import *

from typing import List
'''

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    total=sum(arr)
    if total-d<0 or (total-d)%2:
        return 0
    k=(sum(arr)-d)//2
    mod=(int(1e9)+7)
    prev=[0 for i in range(k + 1)]
    if arr[0]==0:
        prev[0]=2
    else:
        prev[0]=1
    if arr[0]<=k and arr[0]!=0:
        prev[arr[0]]=1
    for i in range(1,n):
        cur=[0 for i in range(k + 1)]
        cur[0]=1
        for t in range(1,k+1):
            nottaken=prev[t]
            taken=0
            if arr[i]<=t:
                taken=prev[t-arr[i]]
            cur[t]=(taken+nottaken)%mod
        prev=cur
    return (prev[k])%mod'''

mod =int(1e9+7)

def findWays(num, tar):
    n = len(num)

    prev = [0] * (tar + 1)
    
    if num[0] == 0:
        prev[0] = 2  # 2 cases - pick and not pick
    else:
        prev[0] = 1  # 1 case - not pick
    
    if num[0] != 0 and num[0] <= tar:
        prev[num[0]] = 1  # 1 case - pick
    
    for ind in range(1, n):
        cur = [0] * (tar + 1)
        for target in range(tar + 1):
            notTaken = prev[target]
    
            taken = 0
            if num[ind] <= target:
                taken = prev[target - num[ind]]
        
            cur[target] = (notTaken + taken) % mod
        prev = cur
    return prev[tar]

def countPartitions(n, d, arr):
    totSum = 0
    for i in range(n):
        totSum += arr[i]
    
    # Checking for edge cases
    if totSum - d < 0 or (totSum - d) % 2:
        return 0
    
    return findWays(arr, (totSum - d) // 2)
    
