class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1
        if val < self.minimum:
            self.minimum = val

    def pop(self) -> None:
        if self.length > 0:
            self.stack.pop(-1)
            self.length -= 1
            if self.length > 0:
                self.minimum = min(self.stack)
            else:
                self.minimum = float('inf')
        

    def top(self) -> int:
        if self.length > 0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.length > 0:
            return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()