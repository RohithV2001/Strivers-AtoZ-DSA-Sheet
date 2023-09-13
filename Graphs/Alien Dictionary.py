#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
        adj=[[] for _ in range(K)]
        indegree=[0]*K
        for i in range(N-1):
            s1=alien_dict[i]
            s2=alien_dict[i+1]
            mx=min(len(s1),len(s2))
            for j in range(mx):
                if s1[j]!=s2[j]:
                    adj[ord(s1[j])-ord('a')].append(ord(s2[j])-ord('a'))
                    break
        V=K
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            node=q.pop(0)
            ans.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        l=''
        for i in ans:
            l=l+chr(i+ord('a'))
        return l

