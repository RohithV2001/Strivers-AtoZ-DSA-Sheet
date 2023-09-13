class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[]
        for i in range(n):
            l=[float('inf')]*n
            dist.append(l)
        for i in edges:
            u=i[0]
            v=i[1]
            wt=i[2]
            dist[u][v]=wt
            dist[v][u]=wt
        for i in range(n):
            dist[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]!=float('inf') and dist[k][j]!=float('inf'):
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        city=-1
        citycount=n
        for i in range(n):
            cnt=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    cnt+=1
            if cnt<=citycount:
                citycount=cnt
                city=i
        return city
        
