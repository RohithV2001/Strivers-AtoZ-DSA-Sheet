quickSort(input, 0, size - 1);
from typing import List

def partitionArray(input: List[int], start: int, end: int) -> int:
    pivot=input[end]
    i=start-1
    for j in range(start,end):
        if input[j]<pivot:
            i+=1
            input[j],input[i]=input[i],input[j]
    input[i+1],input[end]=input[end],input[i+1]
    return i+1



def quickSort(input: List[int], start: int, end: int):
    if start<end:
        pi=partitionArray(input,start,end)
        quickSort(input,start,pi-1)
        quickSort(input,pi+1,end)
