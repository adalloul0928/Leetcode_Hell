class Solution:
    def longestOnes(self, A, K) -> int:
        maxOnes = 0
        onesLeft = K

        pointerLeft = 0
        pointerRight = 0

        while pointerRight < len(A):
            if A[pointerRight] == 1:
                pointerRight += 1
                maxOnes = max(pointerRight - pointerLeft, maxOnes)
            else:
                if onesLeft > 0:
                    onesLeft -= 1
                    pointerRight += 1
                    maxOnes = max(pointerRight - pointerLeft, maxOnes)
                else:
                    # print("Pointer R: {}, Pointer L: {}".format(pointerRight, pointerLeft))
                    while pointerLeft <= pointerRight and onesLeft == 0:
                        if A[pointerLeft] == 0:
                            onesLeft += 1
                        pointerLeft += 1
        return maxOnes

sol = Solution()
input = [0,0,0,1]
k = 4
# input = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
print(sol.longestOnes(input, k))