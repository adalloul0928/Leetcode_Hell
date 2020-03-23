class LRUCache:

    def __init__(self, capacity: int):
        self.order = []
        self.cap = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.order.remove(key)
            self.order.append(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap > 0:
            if key in self.d:
                self.order.remove(key)
                self.order.append(key)
                self.d[key] = value
            else:
                self.d[key] = value
                self.order.append(key)
                self.cap -= 1
        else:
            oldest = self.order.pop(0)
            del self.d[oldest]
            self.d[key] = value
            self.order.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

sol = LRUCache()
inputKey = 5
print(sol.get(inputKey))