class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        ans=[]
        stack=[]
        for i in nums2:
            while stack and stack[-1]<i:
                d[stack.pop()]=i
            stack.append(i)
        for i in nums1:
            ans.append(d.get(i,-1))
        return ans
