class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit=set()
        cur=deque()
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]==1:
                    visit.add((i,j))
                if grid[i][j]==2:
                    cur.append((i,j))
        res=0
        while visit and cur:
            for _ in range(len(cur)):
                i,j=cur.popleft()
                for cd in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if cd in visit:
                        visit.remove(cd)
                        cur.append(cd)
            res+=1
        if visit:
            return -1
        else:
            return res
