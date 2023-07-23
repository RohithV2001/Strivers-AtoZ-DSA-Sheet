def maximumOnesRowHelper(row: [int], low: int, high: int) -> int:
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or row[mid - 1] == 0) and row[mid] == 1:
            return mid
        elif row[mid] == 0:
            return maximumOnesRowHelper(row, (mid + 1), high)
        else:
            return maximumOnesRowHelper(row, low, (mid - 1))
    return -1

def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    ans = -1
    j = maximumOnesRowHelper(matrix[0], 0, m - 1)
    if j == -1:
        j = m
    else:
        ans = 0
    for i in range(1, n):
        while j > 0 and matrix[i][j - 1] == 1:
            j = j - 1
            ans = i
    return ans

    
