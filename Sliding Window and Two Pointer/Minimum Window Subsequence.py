def minWindow(S, T):
    str1=S
    str2=T
    n1=len(str1)
    n2=len(str2)
    i=0
    j=0
    start=-1
    ans=""
    mx=99999 
    while i<n1:
        if str2[j]==str1[i]:
            if j==0: #To Store Starting Index
                start=i
            if j==n2-1 and mx>i-start+1: #if j reaches end updating the ans and updating the window
                mx=i-start+1
                ans=str1[start:i+1]
                i=start #Moving left pointer
            j=(j+1)%n2 #Updating j pointer to initial state if it reaches end 
        i+=1
    return ans
