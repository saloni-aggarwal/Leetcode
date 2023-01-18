class MRUQueue:

    def __init__(self, n: int):
        self.queue = []
        for i in range(1, n+1):
            self.queue.append(i)        

    def fetch(self, k: int) -> int:
        # print("self.queue =", self.queue)
        # print("k =", k)
        ele = self.queue.pop(k-1)
        self.queue.append(ele)
        return ele
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)