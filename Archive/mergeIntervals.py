class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        l = len(intervals)
        i = 0
        while i < l -1:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][0] <= intervals[i+1][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals.pop(i+1)
                l -= 1
            else:
                i += 1
        return intervals

sol = Solution()
input = [[1,4],[4,5]]
print(sol.merge(input))
