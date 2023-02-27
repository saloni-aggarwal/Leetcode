class MyHashSet:

    def __init__(self):
        self.keys = []
        self.values = []

    def add(self, key: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(0)
        else:
            idx = self.keys.index(key)
            self.values[idx] += 1                

    def remove(self, key: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.values[idx]

    def contains(self, key: int) -> bool:
        return True if key in self.keys else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)