import heapq
# NOT COMPLETE BUT CLOSE

class Solution:
    def kClosest(self, points, K):


    def kClosest2(self, points, K):
        myHeap = []
        retArray = []
        for point in points:
            if len(myHeap) < K:
                heapq.heappush(myHeap, (point[0]**2 + point[1]**2, point))
            else:
                peekNum = myHeap[0][0]
                currNum = point[0]**2 + point[1]**2
                if currNum < peekNum:
                    heapq.heappop(myHeap)
                    heapq.heappush(myHeap, (point[0]**2 + point[1]**2, point))

        retArray = [x[1] for x in myHeap]
        return retArray

input = [[1,3],[-2,2]]
k = 1
sol = Solution()
print(sol.kClosest(input, k))