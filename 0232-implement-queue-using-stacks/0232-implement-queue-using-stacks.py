class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ele = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ele

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ele = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ele        

    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()