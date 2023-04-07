class Allocator:

    def __init__(self, n: int):
        self.space = [None] * n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(len(self.space)):
            if self.space[i] == None:
                cnt += 1
            else:
                cnt = 0
            if cnt == size:     
                self.space[i+1-cnt:i+1] = [mID] * size
                return i+1-cnt
            
                
        return -1
        

    def free(self, mID: int) -> int:
        t = 0
        for i in range(len(self.space)):
            if self.space[i] == mID:
                self.space[i] = None
                t += 1
        return t


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)