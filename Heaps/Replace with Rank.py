
def replaceWithRank(n, arr):
    l=[]
    for i in range(n):
        heapq.heappush(l,(arr[i],i))
    currank=0
    curele=-99999
    ans=[0]*len(arr)
    while l:
        num,idx=heapq.heappop(l)
        if num==curele:
            ans[idx]=currank
        else:
            currank+=1
            curele=num
            ans[idx]=currank
    return ans
