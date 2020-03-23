from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeList = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeList[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        mylist = self.timeList.get(key, None)
        if not mylist:
            return ""
        ind = bisect.bisect(mylist, (timestamp, chr(127)))
        return mylist[ind-1][1] if ind else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10]
# ,["love",15],["love",20],["love",25]]