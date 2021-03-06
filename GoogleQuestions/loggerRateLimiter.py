class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logWords = {}
        self.timer = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.logWords:
            self.logWords[message] = timestamp
            return True

        if self.lowWords[message] - 10 > timestamp:
            self.logWords[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)