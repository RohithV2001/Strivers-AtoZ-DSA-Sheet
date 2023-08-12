class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        fa=[0]*n
        for i in range((2*n)-1,-1,-1):
            while len(st)!=0 and st[-1]<=nums[i%n]:
                st.pop()
            if i<n:
                if len(st)!=0:
                    fa[i]=st[-1]
                else:
                    fa[i]=-1
            st.append(nums[i%n])
        return fa
