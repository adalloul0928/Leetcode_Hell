import heapq

class Solution:
    def kClosest(self, points, K):
        heap = []

        for point in points:
            val = abs(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (val, point))

        return [x[1] for x in heapq.nsmallest(K, heap)]