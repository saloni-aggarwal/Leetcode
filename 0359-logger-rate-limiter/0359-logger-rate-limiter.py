class Logger:

    def __init__(self):
        self.nextTimeStamp = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.nextTimeStamp and self.nextTimeStamp[message] > timestamp:
            return False
        self.nextTimeStamp[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)