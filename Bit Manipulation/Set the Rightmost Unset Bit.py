from typing import *

def setBits(N : int) -> int:
    n=N&(N+1)
    if n==0:
        return N
    else:
        return N+1 | N
