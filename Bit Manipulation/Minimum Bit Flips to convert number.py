class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=start^goal
        c=0
        while x>0:
            c+=x&1
            x>>=1
        return c
