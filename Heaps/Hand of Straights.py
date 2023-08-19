class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        count=Counter(hand)
        while count:
            s=min(count.keys())
            k=groupSize
            while k:
                if s not in count:
                    return False
                count[s]-=1
                if not count[s]:
                    del count[s]
                s+=1
                k-=1
        return True
        '''
        if len(hand)%groupSize:
            return False
        count=Counter(hand)
        minh=list(count.keys())
        heapq.heapify(minh)
        while minh:
            first=minh[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minh[0]:
                        return False
                    heapq.heappop(minh)
        return True
