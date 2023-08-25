class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        merged=intervals[0]
        c=0
        for i in range(1,len(intervals)):
            if merged[1] > intervals[i][0]:
                c+=1
            else:
                merged=intervals[i]
        return c
