from math import *
from collections import *
from sys import *
from os import *
import heapq

n=int(input())
p=int(input())
l=list(map(int,input().split()))
heapq.heapify(l)
ans=0
while len(l)>1:
    f=heapq.heappop(l)
    s=heapq.heappop(l)
    ans+=f+s
    heapq.heappush(l,f+s)
print(ans)
