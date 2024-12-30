class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]

            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)
        return res
# Time complexity: O(nlogn) for sorting the intervals   
        
