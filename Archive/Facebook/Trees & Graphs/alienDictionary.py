from collections import defaultdict
from collections import deque

class Solution:
    def alienOrder(self, words) -> str:
        result = ""
        if not words:
            return result

        # to store the graph
        G = defaultdict(list)
        # for the BFS search
        Q = deque()
        # inDegrees for every node
        inDegrees = {}

        for word in words:
            for letter in word:
                inDegrees[letter] = 0

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for ind in range(min(len(word1), len(word2))):
                parent = word1[ind]
                child = word2[ind]
                if word1[ind] != word2[ind]:
                    G[parent].append(child)
                    inDegrees[child] += 1
                    break

        sources = deque()
        for key, val in inDegrees.items():
            if val == 0:
                sources.append(key)

        while sources:
            result += sources[0]
            curr = sources.popleft()
            for child in G[curr]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)
                    del inDegrees[child]

        if len(result) != len(G):
            return ""
        return result

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
sol = Solution()
print(sol.alienOrder(words))