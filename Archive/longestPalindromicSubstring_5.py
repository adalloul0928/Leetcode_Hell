# Question #5 (find the length of the longest palindromic substring)
# NOT WORKING

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        else:
            L = 0
            R = 0
            longestPalindrome = s[0]
            while R < len(s) and L >= 0:
                if s[R] != s[L] and R-L == 0:
                    R += 1
                elif s[R] != s[L] and R-L == 1:
                    L += 1
                if s[R] == s[L]:
                    tempR = R
                    tempL = L
                    while tempR < len(s) and tempL >= 0:
                        tempWord = s[L:R+1]
                        if tempWord == tempWord[::-1] and len(tempWord) > len(longestPalindrome):
                            longestPalindrome = tempWord
                        tempR = tempR + 1
                        tempWord = s[L:R + 1]
                        if R < len(s) and tempWord == tempWord[::-1] and len(tempWord) > len(longestPalindrome):
                            longestPalindrome = tempWord
                        tempL = tempR
                    R += 1
                    L = R
        return longestPalindrome

S = Solution()
print(S.longestPalindrome("aaaa"))