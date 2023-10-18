def evaluateExp(exp: str) -> int:
    n = len(exp)
    mod = 1000000007
    
    # Create a 3D DP array to store the results of subproblems
    dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    
    # Iterate over the expression string
    for i in range(n - 1, -1, -1):
        for j in range(n):
            # Base case 1: Skip invalid ranges
            if i > j:
                continue
            
            # Iterate over possible values of 'isTrue' (0 or 1)
            for isTrue in range(2):
                # Base case 2: When i == j
                if i == j:
                    if isTrue == 1:
                        dp[i][j][isTrue] = int(exp[i] == 'T')
                    else:
                        dp[i][j][isTrue] = int(exp[i] == 'F')
                    continue
                
                # Recurrence logic
                ways = 0
                for ind in range(i + 1, j, 2):
                    lT = dp[i][ind - 1][1]
                    lF = dp[i][ind - 1][0]
                    rT = dp[ind + 1][j][1]
                    rF = dp[ind + 1][j][0]

                    if exp[ind] == '&':
                        if isTrue:
                            ways = (ways + (lT * rT) % mod) % mod
                        else:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lF * rF) % mod) % mod
                    elif exp[ind] == '|':
                        if isTrue:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lT * rT) % mod) % mod
                        else:
                            ways = (ways + (lF * rF) % mod) % mod
                    else:
                        if isTrue:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod) % mod
                        else:
                            ways = (ways + (lF * rF) % mod + (lT * rT) % mod) % mod
                
                dp[i][j][isTrue] = ways
    
    # The final result is stored in dp[0][n - 1][1] when the expression is considered true
    return dp[0][n - 1][1]
