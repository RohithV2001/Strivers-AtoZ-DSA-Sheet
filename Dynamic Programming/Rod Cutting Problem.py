from sys import stdin
import sys

def cutRod(price, n):
    val=price
    W=n
    wt=[]
    for i in range(1,n+1):
        wt.append(i)
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

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
