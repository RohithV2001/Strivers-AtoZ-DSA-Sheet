def firstOccurence(text:str, pat: str) -> int:
    n=len(text)
    m=len(pat)
    for i in range(n):
        if text[i:i+m]==pat:
            return i
    return -1

