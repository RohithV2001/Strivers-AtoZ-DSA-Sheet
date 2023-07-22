class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #Binary Search
        l=0
        r=len(arr)
        while l<r:
            m=(l+r)>>1
            if arr[m]-m-1>=k:
                r=m
            else:
                l=m+1
        return l+k
        #Brute Force
        for i in arr:
            if i<=k:
                k+=1
            else:
                break
        return k
