#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        if start==end:
            return 0
        q=[]
        q.append([start,0])
        dist=[float('inf')]*(10**5)
        dist[start]=0
        while q:
            node,step=q.pop(0)
            for i in arr:
                num=(node*i)%(10**5)
                if step+1<dist[num]:
                    dist[num]=step+1
                    if num==end:
                        return step+1
                    q.append([num,step+1])
        return -1
            
