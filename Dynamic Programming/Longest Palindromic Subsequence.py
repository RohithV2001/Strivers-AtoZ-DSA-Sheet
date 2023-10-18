class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1=s
        s2=s[::-1]
        n = len(s1)
        m = len(s2)
        prev = [0] * (m + 1)
        cur = [0] * (m + 1)
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    cur[ind2] = 1 + prev[ind2 - 1]
                else:
                    cur[ind2] = max(prev[ind2], cur[ind2 - 1])
            prev = cur[:]  
        return prev[m]
        
