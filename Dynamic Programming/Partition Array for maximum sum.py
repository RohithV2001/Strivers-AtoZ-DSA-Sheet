class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for ind in range(n - 1, -1, -1):
            len_val = 0
            max_val = float('-inf')
            max_ans = float('-inf')

            for j in range(ind, min(ind + k, n)):
                len_val += 1
                max_val = max(max_val, arr[j])
                summation = len_val * max_val + dp[j + 1]
                max_ans = max(max_ans, summation)

            dp[ind] = max_ans

        return dp[0]
        
