def isKthBitSet(n: int, k: int) -> bool:
    if n&(1<<(k-1)):
        return True
    return False
