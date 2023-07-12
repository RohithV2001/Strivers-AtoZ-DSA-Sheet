gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
n,m=map(int,input().split())
print(gcd(n,m))
