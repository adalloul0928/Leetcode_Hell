from collections import defaultdict

class Solution:
    def isUnique(self, input):
        d = defaultdict(int)
        for x in input:
            d[x] += 1
            if d[x] > 1:
                return False
        return True


# input = [1,2,3,4]
input = [1,2,3,1]
sol = Solution()
print(sol.isUnique(input))