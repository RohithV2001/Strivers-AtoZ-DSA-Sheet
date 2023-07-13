def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    mn=float('inf')
    mx=float('-inf')
    smn=float('inf')
    smx=float('-inf')
    for i in range(n):
        mn=min(mn,a[i])
        mx=max(mx,a[i])
    for i in a:
        if i<smn and i!=mn:
            smn=i
        if i>smx and i!=mx:
            smx=i
    return smx,smn

    
