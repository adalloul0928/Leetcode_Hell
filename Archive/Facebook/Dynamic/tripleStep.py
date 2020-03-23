class Solution:
    def tripleStep(self, n):
        memo = [0 for x in range(n+1)]

        def tripleRecursive(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            elif memo[n] > 0:
                return memo[n]
            else:
                memo[n] = tripleRecursive(n-3) + tripleRecursive(n-2) + tripleRecursive(n-1)
                return memo[n]

        tripleRecursive(n)
        return memo[n]

sol = Solution()
input = 9
print(sol.tripleStep(9))


