import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictRandom = {}
        self.arr = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dictRandom:
            return False

        self.dictRandom[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dictRandom:
            lastElemVal = self.arr[-1]
            delValIdx = self.dictRandom[val]
            self.arr[delValIdx] = lastElemVal
            self.dictRandom[lastElemVal] = delValIdx
            del self.dictRandom[val]
            self.arr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()