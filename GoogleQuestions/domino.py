class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return -1
        if len(A) == 1:
            if A[0] == A[1]:
                return 0
            else:
                return -1

        minA = 0
        minB = 0
        minABool = True
        minBBool = True

        for ind in range(1, len(A)):
            if A[ind] == A[0]:
                continue
            elif B[ind] == A[0]:
                minA += 1
            else:
                minABool = False
                break

        for ind in range(1, len(B)):
            if B[ind] == B[0]:
                continue
            elif A[ind] == B[0]
                minB += 1
            else:
                minBBool = False
                break

        if minBBool and minABool:
            return min(minA, minB)
        elif minABool:
            return minA
        elif minBBool:
            return minB
        else:
            return -1

sol = Solution()
