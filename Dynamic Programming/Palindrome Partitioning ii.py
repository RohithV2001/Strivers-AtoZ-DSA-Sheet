class Solution:
    def minCut(self, s: str) -> int:
        n  = len(s)
        is_palindrome = [[False] * n for _ in range(n)] 
        min_cuts = [0] * n  

        for j in range(n):
            min_cuts[j] = j  
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or is_palindrome[i + 1][j - 1]):
                    is_palindrome[i][j] = True
                    if i == 0:
                        min_cuts[j] = 0  
                    else:
                        min_cuts[j] = min(min_cuts[j], min_cuts[i - 1] + 1)

        return min_cuts[n - 1]
