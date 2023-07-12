from typing import List

def sumFirstN(n: int) -> int:
    return recursum(n)
def recursum(n):
    if n<=1:
        return n
    return n+recursum(n-1)
