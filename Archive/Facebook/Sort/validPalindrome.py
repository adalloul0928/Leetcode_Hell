import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        punct = string.punctuation

        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l >= len(s) and r < 0:
                return True
            if s[l] != s[r]:

                return False
            l += 1
            r -= 1
        return True



input = "A man, a plan, a canal: Panama"
# input = ".,"
# input = "0P"
sol = Solution()
print(sol.isPalindrome(input))

