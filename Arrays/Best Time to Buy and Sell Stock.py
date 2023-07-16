class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        mx=0
        while right<len(prices):
            cp=prices[right]-prices[left]
            if prices[left]<prices[right]:
                mx=max(cp,mx)
            else:
                left=right
            right+=1
        return mx
