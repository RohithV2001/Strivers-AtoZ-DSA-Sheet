#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        dist=[10**8]*V
        dist[S]=0
        for i in range(V-1):
            for i in edges:
                u=i[0]
                v=i[1]
                wt=i[2]
                if dist[u]!=10**8 and dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
        for i in edges:
            u=i[0]
            v=i[1]
            wt=i[2]
            if dist[u]!=10**8 and dist[u]+wt<dist[v]:
                    temp=[-1]
                    return temp
        return dist
