class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = len(intervals)
        i = 0
        intervals.sort()
        while i < n-1:
            while intervals[i][0] == intervals[i+1][0]:
                ans -= 1
                i += 1
            j = i+1
            while j< n and intervals[i][1] >= intervals[j][1]:
                ans -= 1
                j += 1
            i = j
        return ans