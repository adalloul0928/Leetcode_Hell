from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        primes = {'a': 2,
                  'b': 3,
                  'c': 5,
                  'd': 7,
                  'e': 11,
                  'f': 13,
                  'g': 17,
                  'h': 19,
                  'i': 23,
                  'j': 29,
                  'k': 31,
                  'l': 37,
                  'm': 41,
                  'n': 43,
                  'o': 47,
                  'p': 53,
                  'q': 59,
                  'r': 61,
                  's': 67,
                  't': 71,
                  'u': 73,
                  'v': 79,
                  'w': 83,
                  'x': 89,
                  'y': 97,
                  'z': 101
                  }

        hashWords = defaultdict(list)

        for word in strs:
            tempCount = 1
            for letter in word:
                tempCount *= primes[letter]
            hashWords[tempCount].append(word)

        return [hashWords[index] for index in hashWords]