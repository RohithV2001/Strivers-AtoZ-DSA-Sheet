class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        prev=[0]*(amount+1)
        for i in range(amount+1):
            prev[i]=int((i%coins[0]==0))
                #prev[i]=1
        for i in range(1,n):
            cur=[0]*(amount+1)
            for j in range(amount+1):
                notTake=prev[j]
                take=0
                if coins[i]<=j:
                    take=cur[j-coins[i]]
                cur[j]=take+notTake
            prev=cur
        return prev[amount]
        
