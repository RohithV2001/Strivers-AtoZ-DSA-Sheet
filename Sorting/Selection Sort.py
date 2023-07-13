from typing import List

def selectionSort(arr: List[int]) -> None: 
    for i in range(len(arr)):
        min_id=i
        for j in range(i+1,len(arr)):
            if  arr[j]<arr[min_id]:
                min_id=j
        arr[i],arr[min_id]=arr[min_id],arr[i]
    return arr
