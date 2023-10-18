class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        '''
        cuts.sort()
        cuts = [0] + cuts + [n]

        stick_len = len(cuts)

        dp = [[0]* stick_len for _ in range(stick_len)]

        for i in range(stick_len - 2, -1, -1):
            for j in range(i + 2, stick_len):
                min_cost = float("inf")
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost

        return dp[0][stick_len - 1]'''
        c=len(cuts)
        cuts = [0] + cuts + [n]
        cuts.sort()
        # Create a 2D DP table initialized with zeros
        dp = [[0] * (c + 2) for _ in range(c + 2)]

        # Calculate the minimum cost using dynamic programming
        for i in range(c, -1, -1):
            for j in range(1, c + 1):
                if i > j:
                    continue
                
                mini = float('inf')
                
                for ind in range(i, j + 1):
                    ans = cuts[j + 1] - cuts[i - 1] + dp[i][ind - 1] + dp[ind + 1][j]
                    mini = min(mini, ans)
                
                dp[i][j] = mini
        
        return dp[1][c]
