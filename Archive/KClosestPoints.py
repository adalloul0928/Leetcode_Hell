class Solution:
    def kClosest(self, points, K):
        ans = []
        for x in points:
            temp = x[0] + x[1]