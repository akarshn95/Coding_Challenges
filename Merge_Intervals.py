class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        
        intervals.sort(key =lambda x:x[0])
        res = []
        for interval in intervals:
            # no overlap
            if not res or res[-1][1] < interval [0]:
                res.append(interval)
            else:
            # merging  
                res[-1][1] = max(res[-1][1], interval[1])
        return res
