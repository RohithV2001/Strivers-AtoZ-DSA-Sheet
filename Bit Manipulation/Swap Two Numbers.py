def swapNumber(a:int,  b: int) -> None:
    a=(a^b)
    b=(a^b)
    a=(a^b)
    return (a,b)
