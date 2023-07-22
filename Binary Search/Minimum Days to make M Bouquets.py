class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def md(s):
            f=0
            b=0
            for i in bloomDay:
                if i>s:
                    f=0
                else:
                    b+=(f+1)//k
                    f=(f+1)%k
            return b>=m
        if m*k>len(bloomDay):
            return -1
        l=1
        h=max(bloomDay)
        while l<h:
            mid=l+(h-l)//2
            if md(mid):
                h=mid
            else:
                l=mid+1
        return l
