from typing import *

def bitManipulation(num : int, i : int) -> List[int]:
    ans=[-1]*3
    n=1<<(i-1)
    bit1=num&n
    if bit1>0:
        ans[0]=1
    else:
        ans[0]=0
    if ans[0]==0:
        ans[2]=num
        ans[1]=num | n
    else:
        ans[1]=num
        ans[2]=num&(~n)
    return ans
