class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals):
            intervals.sort(key=lambda x:x[0])
            merged=[]
            for interval in intervals:
                if not merged or merged[-1][1] < interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] =max(merged[-1][1], interval[1])
            return merged
        intervals.append(newInterval)
        ans=merge(intervals)
        return ans
        '''O(n)'''
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        ans=[]
        i=0

        while i<len(intervals) and newInterval[0]>intervals[i][1]:
            ans.append(intervals[i])
            i+=1
            
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i+=1
        ans.append(newInterval)

        while i<len(intervals):
            ans.append(intervals[i])
            i+=1
        print(ans)
