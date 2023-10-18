class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def compare(s1, s2):
            if len(s1) != len(s2) + 1:
                return False
            first = 0
            second = 0
            while first < len(s1):
                if second < len(s2) and s1[first] == s2[second]:
                    first += 1
                    second += 1
                else:
                    first += 1
            return first == len(s1) and second == len(s2)
        n=len(words)
        dp=[1 for _ in range(n)]
        words.sort(key=len)
        ans=0
        for i in range(n):
            for prev in range(i):
                if compare(words[i],words[prev]) and dp[prev]+1>dp[i]:
                    dp[i]=1+dp[prev]
            if dp[i]>ans:
                ans=dp[i]
        return ans
