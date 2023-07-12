n=int(input())
f=n
k=len(str(n))
s=0
while n!=0:
    d=n%10
    s=s+(d**k)
    n=n//10
if f==s:
    print("true")
else:
    print("false")
