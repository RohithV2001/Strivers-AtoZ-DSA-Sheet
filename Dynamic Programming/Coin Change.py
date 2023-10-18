class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        prev=[0]*(amount+1)
        cur=[0]*(amount+1)
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=i//coins[0]
            else:
                prev[i]=int(1e9)
        for i in range(1,n):
            for j in range(amount+1):
                notTaken=prev[j]
                taken=int(1e9)
                if coins[i]<=j:
                    taken=1+cur[j-coins[i]]
                cur[j]=min(taken,notTaken)
            prev=cur
        if prev[amount]>=int(1e9):
            return -1
        return prev[amount]
