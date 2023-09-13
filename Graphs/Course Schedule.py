class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            adj[x].append(y)
        V=len(adj)
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        cnt=0
        while q:
            node=q.pop(0)
            ans.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            cnt+=1
        if len(ans)==V:
            return True
        else:
            return False
