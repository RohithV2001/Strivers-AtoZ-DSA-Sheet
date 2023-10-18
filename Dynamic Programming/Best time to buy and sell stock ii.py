class Solution(object):
    def maxProfit(self, prices):
        n=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                n+=prices[i]-prices[i-1]
        return n
        
