class Solution:
    def factorial (self, N):
        if N==0:
            return 1
        return N*self.factorial(N-1)
