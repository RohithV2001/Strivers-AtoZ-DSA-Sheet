def countPrimes(n: int) -> int:
    l=[]
    def prime(n):
        while n%2==0:
            if 2 not in l:
                l.append(2)
            n=n/2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                if i not in l:
                    l.append(i)
                n = n / i
        if n>1:
            l.append(int(n))
    prime(n)   
    return l
