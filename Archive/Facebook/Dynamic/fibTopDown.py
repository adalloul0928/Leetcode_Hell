class Solution:
    def fib(self, n):
        memo = [0 for i in range(n+1)]

        def fibRecursive(n):
            if n == 0 or n == 1:
                return 1
            elif (memo[n] == 0):
                memo[n] = fibRecursive(n-1) + fibRecursive(n-2)
            return memo[n]
        fibRecursive(n)
        return memo[n]

sol = Solution()
input = 10
print(sol.fib(input))