import heapq

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda input: input[0])
        heap = [intervals[0][1]]
        count = 1

        for i in range(1, len(intervals)):
            minItemHeap = heap[0]
            newItem = intervals[i]
            if minItemHeap > newItem[0]:
                heapq.heappush(heap, newItem[1])
                count += 1
            else:
                heapq.heappushpop(heap, newItem[1])
        return count

sol = Solution()
input = [[0,30],[5,10],[15,20]]
print(sol.minMeetingRooms(input))