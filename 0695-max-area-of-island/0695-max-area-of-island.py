class Solution:
    def totalArea(self, grid, x, y, m, n, total):
        if grid[x][y] == 0:
            return 0       
        grid[x][y] = 0
        total += 1
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for dirX, dirY in dirs:
            currX, currY = x+dirX, y+dirY
            if 0 <= currX < m and 0 <= currY < n:
                total = max(total, self.totalArea(grid, currX, currY, m, n, total))
                
        return total
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    ans = max(ans, self.totalArea(grid, x, y, m, n, 0))
        
        return ans
         
        