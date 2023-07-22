import math
def floorSqrt(n):
   low=0
   high=n
   while low<=high:
      mid=(low+high)//2
      val=mid*mid
      if val<=n:
         low=mid+1
      else:
         high=mid-1
   return high
n= int(input())
print(floorSqrt(n))
