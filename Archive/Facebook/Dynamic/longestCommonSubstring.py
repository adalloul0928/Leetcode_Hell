class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        maxPalindrome = 1
        start_i = 0

        palindromeArray = [[False for i in range(len(s))]for i in range(len(s))]

        """case1: len of substring == 1 ... that's a palindrome...diagonal willbe True"""
        for i in range(len(s)):
            palindromeArray[i][i] = True

        """case2: len of substring == 2 ... check if it's a palindrome"""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                palindromeArray[i][i+1] = True
                maxPalindrome = 2
                start_i = i

        """case3: len of substring from 3 to len(s) ... check if palindrome"""
        for j in range(len(s)):
            for i in range(len(s)):
                if i < j:
                    if s[i] == s[j] and palindromeArray[i+1][j-1] == True:
                        palindromeArray[i][j] = True
                        if j-i+1 > maxPalindrome:
                            maxPalindrome = j-i+1
                            start_i = i

        return s[start_i: start_i + maxPalindrome]

input = 'abbabbbbb'
sol = Solution()
print(sol.longestPalindrome(input))