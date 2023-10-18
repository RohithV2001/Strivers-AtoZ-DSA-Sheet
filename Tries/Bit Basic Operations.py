def getXOR(a: int, b: int) -> int:
    return a^b

def getBit(c: int, d: int) -> int:
    m=1<<c 
    if d & m==0:
        return 0
    return 1 

def setBit(e: int, f: int) -> int:
    m=1<<e
    return f | m
