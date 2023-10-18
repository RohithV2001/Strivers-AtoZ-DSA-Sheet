from typing import List

def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    dp1 = [1] * n
    dp2 = [1] * n

    # Calculate the length of the longest increasing subsequence
    for i in range(n):
        for prev_index in range(i):
            if arr[prev_index] < arr[i]:
                dp1[i] = max(dp1[i], 1 + dp1[prev_index])

    # Reverse the direction of nested loops to calculate the length of the longest decreasing subsequence
    for i in range(n - 1, -1, -1):
        for prev_index in range(n - 1, i, -1):
            if arr[prev_index] < arr[i]:
                dp2[i] = max(dp2[i], 1 + dp2[prev_index])

    maxi = -1

    # Find the maximum length of bitonic subsequence by combining increasing and decreasing lengths
    for i in range(n):
        maxi = max(maxi, dp1[i] + dp2[i] - 1)

    return maxi
