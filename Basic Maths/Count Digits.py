def countDigits(n: int) -> int:
    c=0
    f=n 
    while n!=0:
        d=n%10
        if d!=0:
            if f%d==0:
                c+=1
        n=n//10
    return c 
