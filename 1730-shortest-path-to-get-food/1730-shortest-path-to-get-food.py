class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = []
        visited = set()
        m, n = len(grid), len(grid[0])
        
        breaker = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    queue.append((i,j))
                    breaker = True
                    break
            if breaker:
                break
          
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
        steps = 0
        
        while queue:
            tempQueue = set()
            while queue:
                oldCorr = queue.pop(0)
                visited.add(oldCorr)
                
                if grid[oldCorr[0]][oldCorr[1]] == "#":
                    return steps
                
                for neigh in neighbors:
                    currX, currY = oldCorr[0] + neigh[0], oldCorr[1] + neigh[1]
                    
                    if 0 <= currX < m and 0 <= currY < n:
                        if grid[currX][currY] == "X" or (currX, currY) in visited:
                            continue
                        
                        tempQueue.add((currX, currY))
                        
            queue = list(tempQueue)
            steps += 1
            
        return -1
            
                