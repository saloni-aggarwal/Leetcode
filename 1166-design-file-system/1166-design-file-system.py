class FileSystem:

    def __init__(self):
        self.pathValues = {}
        

    def createPath(self, path: str, value: int) -> bool:
        if path in self.pathValues:
            return False
        
        pathArray = path.split("/")
        pathArray = pathArray[1:]
        currPath = ""
        
        for p in pathArray[:-1]:
            currPath += "/" + p
            if currPath not in self.pathValues:
                return False
            
        currPath += "/" + pathArray[-1]
        self.pathValues[currPath] = value
        return True
            

    def get(self, path: str) -> int:
        # print(self.pathValues)
        if path not in self.pathValues:
            return -1
        return self.pathValues[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)