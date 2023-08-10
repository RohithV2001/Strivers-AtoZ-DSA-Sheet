def printDivisors(n: int) -> List[int]:
    l=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if n/i==i:
                l.append(i)  
            else:
                l.append(i) 
                l.append(int(n/i))
    l.sort()
    return l
