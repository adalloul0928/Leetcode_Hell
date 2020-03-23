class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        newS = S.replace('-', '')
        R = []
        C = 1
        if len(newS) < K:
            return newS.upper()
        else:
            for x in reversed(newS.upper()):
                R.insert(0, x)
                if C%K == 0 and C != len(newS):
                    R.insert(0,'-')
                C += 1
        return "".join(R)

input = "2-5g-3-J"
K = 2
sol = Solution()
print(sol.licenseKeyFormatting(input, K))