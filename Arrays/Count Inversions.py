from typing import *

def numberOfInversions(a : List[int], n : int) -> int:
    def mergeSort(nums):
            count=0
            if len(nums)>1:
                mid=len(nums)//2
                L=nums[:mid]
                R=nums[mid:]
                count+=mergeSort(L)
                count+=mergeSort(R)
                j=0
                for i in range(len(L)):
                    while j<len(R) and L[i]>R[j]:
                        j+=1
                    count+=j
                i,j,k=0,0,0
                while(i<len(L) and j<len(R)):
                    if L[i]>R[j]:
                        nums[k]=R[j]
                        j+=1
                    else:
                        nums[k]=L[i]
                        i+=1
                    k+=1
                while(i<len(L)):
                    nums[k]=L[i]
                    k+=1
                    i+=1
                while(j<len(R)):
                    nums[k]=R[j]
                    j+=1
                    k+=1
            return count
    return mergeSort(a)
