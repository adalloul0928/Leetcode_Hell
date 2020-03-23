# NOT SOLVED

class Solution:
    def oddEvenJumps(self, A) -> int:
        n = 0
        for j in range(len(A)):
            state = 1
            index = j
            flag = True
            while flag:
                if index == len(A)-1:
                    print(j)
                    n += 1
                    flag = False
                elif state % 2 == 1:
                    index = A.index(min(A[index+1:]))
                    state += 1
                elif state % 2 == 0:
                    index = A.index(max(A[index+1:]))
                    state += 1
                else:
                    flag = False
        return n



input = [2,3,1,1,4]
sol = Solution()
print(sol.oddEvenJumps(input))