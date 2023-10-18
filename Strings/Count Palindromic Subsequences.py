class Solution:
    def countPS(self,string):
        mod=(int(1e9)+7)
        N = len(string)
        cps = [[0 for i in range(N + 1)]for j in range(N + 1)]
        for i in range(N):
            cps[i][i] = 1
        for L in range(2, N + 1):
     
            for i in range(N):
                k = L + i - 1
                if (k < N):
                    if (string[i] == string[k]):
                        cps[i][k] = (cps[i][k - 1] +
                                     cps[i + 1][k] + 1)
                    else:
                        cps[i][k] = (cps[i][k - 1] +
                                     cps[i + 1][k] -
                                     cps[i + 1][k - 1])

        return (cps[0][N - 1])%mod
        

