lass Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=1 if dividend^divisor >=0 else -1
        if dividend<0:
            dividend=-dividend
        if divisor<0:
            divisor=-divisor
        res=0
        for i in range(31,-1,-1):
            if (divisor<<i)<=dividend:
                res+=(1<<i)
                dividend-=(divisor<<i)
        res=res*sign
        if not (-2**31 <=res <=2**31-1):
            return 2**31-1
        else:
            return res
