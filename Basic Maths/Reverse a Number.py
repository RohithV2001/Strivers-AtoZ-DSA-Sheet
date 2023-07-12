class Solution:
    def reverse(self, x: int) -> int:
        n=x
        flag=0
        if x<0:
            flag=1
            x=-x
        rev=0
        while x!=0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if flag==0:
            if rev>((2**31)-1):
                return 0
            else:
                return rev
        else:
            if -rev<(-(2**31)):
                return 0
            else:
                return -rev
