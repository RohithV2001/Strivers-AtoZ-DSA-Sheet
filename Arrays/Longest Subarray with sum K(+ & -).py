from os import *
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    s=0
    mx=0
    d={}
    for i in range(len(nums)):
        s+=nums[i]
        if s==k:
            mx=i+1
        if s not in d:
            d[s]=i
        else:
            mx=max(i-d[s],mx)
    return mx
