A = [3,2,1]
st=[]
ans=[0]*len(A)
for i in range(len(A)):
    while st and st[-1]>=A[i]:
        st.pop()
    if i<len(A):
        if st:
            ans[i]=st[-1]
        else:
            ans[i]=-1
    st.append(A[i])
print(ans)
