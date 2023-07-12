from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    s=0
    e=len(nums)-1
    reversearr(nums,s,e)
    return nums

def reversearr(nums,s,e):
    if s<e:
        nums[s],nums[e]=nums[e],nums[s]
        reversearr(nums,s+1,e-1)
