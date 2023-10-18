class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
    
        # Create a 3D DP table with dimensions (n+1) x 2 x 3 and initialize it to 0 values
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        
        # The base case is already covered as the DP array is initialized to 0
        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    
                    if buy == 0:
                        # We can buy the stock
                        dp[ind][buy][cap] = max(0 + dp[ind + 1][0][cap], -prices[ind] + dp[ind + 1][1][cap])
                    elif buy == 1:
                        # We can sell the stock
                        dp[ind][buy][cap] = max(0 + dp[ind + 1][1][cap], prices[ind] + dp[ind + 1][0][cap - 1])
        
        return dp[0][0][2]
