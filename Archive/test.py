class Solution:
    def waitingTime(self, tickets, p):
        # Write your code here
        total = tickets[p]
        half_1 = tickets[:p]
        half_2 = tickets[p + 1:]
        for n in half_1:
            if n < tickets[p]:
                total += n
            else:
                total += tickets[p]
        for n in half_2:
            if n < tickets[p]:
                total += n
            else:
                total += tickets[p] - 1
        return total

sol = Solution()
input = [1,2,5]
n = 1
print(sol.waitingTime(input, n))
