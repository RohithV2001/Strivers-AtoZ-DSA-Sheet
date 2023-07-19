def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n=len(a)
    d=[0]*(n+1)
    for i in range(len(a)):
        d[a[i]]+=1
    r=-1
    m=-1
    for j in range(1,n+1):
        if d[j]==2:
            r=j
        elif d[j]==0:
            m=j
    return [r,m]
