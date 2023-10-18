from typing import List
def calculate(lps,pattern,m):
    lps[0]=0
    i=1
    len=0
    while i<m:
        if pattern[i]==pattern[len]:
            len+=1
            lps[i]=len
            i+=1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1
def stringMatch(text: str, pattern: str) -> List[int]:
    n=len(text)
    m=len(pattern)
    lps=[0]*m 
    calculate(lps,pattern,m)
    i=0
    j=0
    l=[]
    while (n-i)>=(m-j):
        if pattern[j]==text[i]:
            i+=1
            j+=1
        if j==m:
            l.append(i-j+1)
            j=lps[j-1]
        elif i<n and pattern[j]!=text[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return l
