class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s, i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isValid(s, i+1, j) or isValid(s, i, j-1)
        return True

sol = Solution()
input = "abbca"
print(sol.validPalindrome(input))