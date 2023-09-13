#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q=[]
        q.append(0)
        vis=[0]*V
        vis[0]=1
        bfs=[]
        while q:
            node=q.pop(0)
            bfs.append(node)
            for i in adj[node]:
                if vis[i]==0:
                    vis[i]=1
                    q.append(i)
        return bfs
