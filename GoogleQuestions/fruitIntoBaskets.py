from collections import Counter

class Solution:
    def totalFruit(self, tree) -> int:
        # i is the minimum index variable
        ans = i = 0
        count = Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans