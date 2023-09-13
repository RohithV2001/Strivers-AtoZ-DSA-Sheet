class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        indegree=[0]*V
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
        return ans
        
        '''
        self.vis=[0]*V
        self.adj=adj
        self.st=[]
        def dfs(node):
            self.vis[node]=1
            for i in self.adj[node]:
                if self.vis[i]==0:
                    dfs(i)
            self.st.append(node)
        for i in range(V):
            if self.vis[i]==0:
                dfs(i)
        return self.st[::-1]
        '''

