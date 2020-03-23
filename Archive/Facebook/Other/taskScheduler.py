from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        myTasks = Counter(tasks)
        # retStr = []
        counter = 0
        coolingPeriod = n
        Q = []
        for k in myTasks:
            heapq.heappush(Q, (-myTasks[k], k))

        while Q:
            tempQ = []
            while coolingPeriod >= 0 and Q:
                curr = heapq.heappop(Q)
                currVal = curr[0]
                k = curr[1]
                currVal += 1
                counter += 1
                coolingPeriod -= 1
                if currVal < 0:
                    heapq.heappush(tempQ, (currVal, k))

            while tempQ and coolingPeriod >= 0:
                counter += 1
                coolingPeriod -= 1

            Q = tempQ
            coolingPeriod = n
        return counter


sol = Solution()
input = ["A","A","A","B","B","B"]
n = 0
print(sol.leastInterval(input, n))