lass Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        l=[]
        for i,num in d.items():
            heapq.heappush(l,(-1*num,i))
        ans=[]
        i=0
        while i<k:
            val=heapq.heappop(l)
            ans.append(val[1])
            i+=1
        return ans
        '''
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        p=dict(sorted(d.items(),key=lambda x:x[1],reverse=True)) 
        return list(p)[:k]'''
