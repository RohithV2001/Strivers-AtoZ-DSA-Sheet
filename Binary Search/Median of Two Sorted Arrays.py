class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        def median(nums1,nums2,m,n):
            if m>n:
                return median(nums2,nums1,n,m)
            low=0
            high=m
            medianpos=((m+n)+1)//2
            mid=(low+high)//2
            while low<=high:
                ct1=(low+high)//2
                ct2=medianpos-ct1
                l1=-1e6 if (ct1==0) else nums1[ct1-1]
                l2=-1e6 if (ct2==0) else nums2[ct2-1]
                r1=1e6 if (ct1==m) else nums1[ct1]
                r2=1e6 if (ct2==n) else nums2[ct2]
                if l1<=r2 and l2<=r1:
                    if (m+n)%2==0:
                        return (max(l1,l2)+min(r1,r2))/2
                    else:
                        return max(l1,l2)
                elif l1>r2:
                    high=ct1-1
                else:
                    low=ct1+1
            return 0
        return median(nums1,nums2,m,n)
