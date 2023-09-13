class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        adj=[]
        for i in range(V):
            adj.append([])
        indegree=[0]*V
        for i in range(V):
            for j in graph[i]:
                adj[j].append(i)
                indegree[i]+=1
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
        ans.sort()
        return ans
