class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        firstX, firstY = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    firstX, firstY = i, j
                    break
        
        bfsQueue = [(firstX, firstY)]
        anotherQueue = [(firstX, firstY)]
        grid[firstX][firstY] = 2
        
        while bfsQueue:
            tempQueue = []
            for x, y in bfsQueue:
                for currX, currY in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if currX >= 0 and currX < n and currY >= 0 and currY < n and grid[currX][currY] == 1:
                        tempQueue.append((currX, currY))
                        anotherQueue.append((currX, currY))
                        grid[currX][currY] = 2
            bfsQueue = tempQueue
            
        distance = 0
        
        while anotherQueue:
            tempQueue = []
            for x, y in anotherQueue:
                for currX, currY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if currX >= 0 and currX < n and currY >= 0 and currY < n:
                        if grid[currX][currY] == 1:
                            return distance
                        elif grid[currX][currY] == 0:
                            tempQueue.append((currX, currY))
                            grid[currX][currY] = -1
                            
            
            anotherQueue = tempQueue
            distance += 1
                    
                    
                    
                    
                    
                    