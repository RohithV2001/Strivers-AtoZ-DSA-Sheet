from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totSum = sum(arr)
    
    # Initialize a boolean array 'prev' to store the results for the previous row.
    prev = [False] * (totSum + 1)
    prev[0] = True  # Base case: An empty subset can always achieve a sum of 0.

    # Handle the base case for the first element in the array.
    if arr[0] <= totSum:
        prev[arr[0]] = True

    # Iterate through the elements in the array.
    for ind in range(1, n):
        # Initialize a new boolean array 'cur' for the current row.
        cur = [False] * (totSum + 1)
        cur[0] = True  # An empty subset can always achieve a sum of 0.

        # Fill in the 'cur' array using dynamic programming.
        for target in range(1, totSum + 1):
            # If the current element is not taken, the result is the same as the previous row.
            notTaken = prev[target]

            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = prev[target - arr[ind]] if arr[ind] <= target else False

            # Update the 'cur' array with the result of taking or not taking the current element.
            cur[target] = notTaken or taken

        # Update 'prev' to 'cur' for the next iteration.
        prev = cur

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if prev[i]:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini
