import heapq
class Solution:
    def maxCombinations(self, N, K, A, B):
        ans=[]
        A.sort()
        B.sort()
        l=[]
        n=len(A)
        heapq.heapify(l)
        l.append((-A[n-1]-B[n-1],(n-1,n-1)))
        st=set()
        st.add((n-1,n-1))
        for i in range(K):
            temp=heapq.heappop(l)
            ans.append(-1*temp[0])
            i=temp[1][0]
            j=temp[1][1]
            sm=A[i-1]+B[j]
            temp1=(i-1,j)
            if temp1 not in st:
                heapq.heappush(l,(-sm,temp1))
                st.add(temp1)
            sm=A[i]+B[j-1]
            temp1=(i,j-1)
            if temp1 not in st:
                heapq.heappush(l,(-sm,temp1))
                st.add(temp1)
        return ans
