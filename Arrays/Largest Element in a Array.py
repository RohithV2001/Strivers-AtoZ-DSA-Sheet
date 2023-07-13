from os import *
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    mx=arr[0]
    for i in arr:
        if mx<i:
            mx=i
    return mx 
