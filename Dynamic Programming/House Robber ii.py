class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            n=len(arr)
            prev=arr[0]
            prev2=0
            for i in range(1,n):
                pick=arr[i]
                if i>1:
                    pick+=prev2
                npick=0+prev
                cur=max(pick,npick)
                prev2=prev
                prev=cur
            return prev
        l=len(nums)
        if l<2:
            return nums[0]
        temp=[]
        temp2=[]
        for i in range(l):
            if i!=0:
                temp.append(nums[i])
            if i!=l-1:
                temp2.append(nums[i])
        ans1=solve(temp)
        ans2=solve(temp2)
        return max(ans1,ans2)
