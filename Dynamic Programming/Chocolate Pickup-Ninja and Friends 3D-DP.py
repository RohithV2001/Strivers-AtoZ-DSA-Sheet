from os import *
from sys import *
from collections import *
from math import *
import sys
from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    n=r 
    m=c
    front = [[0] * m for _ in range(m)]
    cur = [[0] * m for _ in range(m)]

    # Initialize the values for the last row of front based on grid values
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                front[j1][j2] = grid[n - 1][j1]
            else:
                front[j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    # Iterate through rows from the second-to-last row to the first row
    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize

                # Try out 9 possible options by changing the indices
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)  # A large negative value if out of bounds
                        else:
                            ans += front[j1 + di][j2 + dj]  # Add the value from the current front row

                        maxi = max(ans, maxi)
                cur[j1][j2] = maxi

        # Update front with the values of cur for the next iteration
        front = [row[:] for row in cur]

    # Return the maximum chocolates collected in the top-left corner of front
    return front[0][m - 1]
