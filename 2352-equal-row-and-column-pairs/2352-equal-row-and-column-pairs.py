class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        columns = []
        n = len(grid)
        
        for i in range(n):
            rows.append(grid[i])
            temp = []          
            columns.append([grid[c][i] for c in range(n)])        
        
        count = 0
        
        for r in range(n):
            for c in range(n):
                count = count + 1 if rows[r] == columns[c] else count
        
        return count
        