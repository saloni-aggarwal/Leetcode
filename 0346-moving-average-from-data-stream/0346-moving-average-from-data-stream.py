class MovingAverage:

    def __init__(self, size: int):
        self.vals = [0] * size
        self.currSize = 0

    def next(self, val: int) -> float:
        # print(self.currSize)
        if self.currSize == len(self.vals):
            self.vals.pop(0)
            self.vals.append(val)
        else:
            self.vals[self.currSize] = val
            self.currSize += 1
            
        return sum(self.vals) / self.currSize
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)