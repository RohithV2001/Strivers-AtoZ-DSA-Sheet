def Prime(d):
    if n<=1:
        return False
    for i in range(2,int(sqrt(d))+1):
        if d%i==0:
            return False
    return True 

n=int(input())
if Prime(n):
    print("YES")
else:
    print("NO")
