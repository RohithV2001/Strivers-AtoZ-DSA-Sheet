class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        ans =[]

        for i in range(2, n):
            if isPrime[i] == True:
                for j in range(i * 2, n, i):
                    isPrime[j] = False
        c=0
        for i in range(2,n):
            if isPrime[i]:
                c+=1
        return c
