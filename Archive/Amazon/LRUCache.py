# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.ordDict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.ordDict:
            self.ordDict.move_to_end(key)
            return self.ordDict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.ordDict[key] = value
        self.ordDict.move_to_end(key)
        if len(self.ordDict) > self.cap:
            self.ordDict.popitem(last=False)