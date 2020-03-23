class Solution:
    # Recursive Slow Solution
    # def climbStairs(self, n: int) -> int:
    #     sum = self.climbStairsHelper(n)
    #     return sum
    #
    # def climbStairsHelper(self, n):
    #     if n == 0:
    #         return 1
    #     elif n < 0:
    #         return 0
    #     else:
    #         return self.climbStairsHelper(n - 2) + self.climbStairsHelper(n - 1)


    # This is simply a fibonacci sequence
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]
        iterator = 2
        if n <= 2:
            return arr[n]
        while iterator <= n:
            arr.append(arr[iterator-1] + arr[iterator-2])
            iterator += 1
        return arr[n]

sol = Solution()
print(sol.climbStairs(5))