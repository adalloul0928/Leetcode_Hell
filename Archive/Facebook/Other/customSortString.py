from collections import Counter
import string

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        letter_count = Counter(T)
        other_letters = set(string.ascii_lowercase) - set(S)
        order = S + ''.join(other_letters)
        result = []

        for letter in order:
            result.extend([letter * letter_count[letter]])
        return ''.join(result)

sol = Solution()
S = "cba"
T = "abcd"
print(sol.customSortString(S, T))