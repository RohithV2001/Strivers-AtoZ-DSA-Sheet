class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mx=sum(cardPoints[:k])
        s=mx
        for i in range(k-1,-1,-1):
            s-=cardPoints[i]
            s+=cardPoints[i-k]
            mx=max(mx,s)
        return mx
