class MinStack:

    def __init__(self):
        self.stack = []
        # self.length = 0
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.length += 1
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.minimum[-1] == self.stack[-1]:
            self.minimum.pop(-1)
        self.stack.pop(-1)
        

    def top(self) -> int:
        # if self.length > 0:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # if self.length > 0:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()