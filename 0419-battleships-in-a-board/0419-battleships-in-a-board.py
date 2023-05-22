class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        battleships = 0
        n, m = len(board), len(board[0])
        
        for i in range(n):
            for j in range(m):
                left = board[i][j-1] if j-1 >= 0 else '.'
                top = board[i-1][j] if i-1 >= 0 else '.'
                if board[i][j] == 'X' and left != 'X' and top != 'X':
                    battleships += 1
                    
        return battleships
        