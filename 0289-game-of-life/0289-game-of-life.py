class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        neighbors = [[0]*n for _ in range(m)]
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [-1,1], [1,-1], [1,1]]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    for dr in dirs:
                        currX, currY = i + dr[0], j + dr[1]
                        if 0 <= currX < m and 0 <= currY < n:
                            neighbors[currX][currY] += 1
                            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 and (neighbors[i][j] < 2 or neighbors[i][j] > 3):
                    board[i][j] = 0
                    
                if board[i][j] == 0 and neighbors[i][j] == 3:
                    board[i][j] = 1