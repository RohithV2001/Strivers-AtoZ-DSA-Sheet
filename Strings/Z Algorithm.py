from typing import List
def getarr(st,z):
    n=len(st)
    l=0
    r=0
    k=0
    for i in range(1,n):
        if i>r:
            l,r=i,i 
            while r<n and st[r-l]==st[r]:
                r+=1
            z[i]=r-l
            r-=1
        else:
            k=i-l 
            if z[k]<r-i+1:
                z[i]=z[k]
            else:
                l=i
                while r<n and st[r-l]==st[r]:
                    r+=1
                z[i]=r-l 
                r-=1
    

def search(s: str, pattern: str) -> List[int]:
    final=pattern+'$'+s 
    l=len(final)
    z=[0]*l
    li=[]
    getarr(final,z)
    for i in range(l):
        if z[i]==len(pattern):
            li.append(i-len(pattern))
    return li
