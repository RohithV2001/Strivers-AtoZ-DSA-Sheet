import math
def sumOfAllDivisors(n: int) -> int:
    ans=0
    for i in range(1,n+1):
        ans+=i*(math.floor((n/i)))
    return ans
