from typing import List
import sys
def knapsack(id,wt,val,n,W,dp):
    if id==0:
        return (W//wt[0])*val[0]
    if dp[id][W]!=-1:
        return dp[id][W]
    notTaken=0+knapsack(id-1,wt,val,n,W,dp)
    taken=-99999999
    if wt[id]<=W:
        taken=val[id]+knapsack(id,wt,val,n,W-wt[id],dp)
    dp[id][W]=max(taken,notTaken)
    return dp[id][W]


def unboundedKnapsack(n, W, val, wt):
    # Create a list 'cur' to store the maximum value for different capacities
    cur = [0] * (W + 1)

    # Initialize the base condition for the first item
    for i in range(wt[0], W + 1):
        cur[i] = (i // wt[0]) * val[0]

    # Fill in the 'cur' list for the remaining items and capacities
    for ind in range(1, n):
        for cap in range(W + 1):
            # Calculate the maximum value when the current item is not taken
            notTaken = cur[cap]

            # Initialize a variable to store the maximum value when the current item is taken
            taken = -sys.maxsize
            if wt[ind] <= cap:
                taken = val[ind] + cur[cap - wt[ind]]

            # Store the maximum of "notTaken" and "taken" in the 'cur' list
            cur[cap] = max(notTaken, taken)

    # The maximum value for the entire knapsack is at 'cur[W]'
    return cur[W]
'''

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    prev=[0]*(w+1)
    for i in range(weight[0],(w+1)):
        prev[i]=(i//weight[0])*profit[0]
    for i in range(1,n):
        cur=[0]*(w+1)
        for j in range(w+1):
            notTake=prev[j]
            take=-9999
            if weight[i]<=j:
                taken=profit[i]+prev[j-weight[i]]
            prev[j]=max(take,notTake)
        #prev=cur
    return prev[w]'''
