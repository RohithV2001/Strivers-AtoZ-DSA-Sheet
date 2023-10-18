from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    prev=0
    prev2=0
    for i in range(1,n):
        j2=float('inf')
        j1=prev+abs(heights[i]-heights[i-1])
        if i>1:
            j2=prev2+abs(heights[i]-heights[i-2])
        cur=min(j1,j2)
        prev2=prev
        prev=cur
    return prev
