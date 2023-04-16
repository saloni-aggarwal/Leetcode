class Solution {
    public void dfs(char[][]grid, int r, int c) {
        if(grid.length == 0)
            return;
        int rc = grid.length;
        int cc = grid[0].length;
        
        if(r < 0 || c < 0 || r >= rc || c >= cc || grid[r][c] == '0') 
            return;
        
        grid[r][c] = '0';
        dfs(grid, r+1, c);
        dfs(grid, r-1, c);
        dfs(grid, r, c+1);
        dfs(grid, r, c-1);
    }
    
    public int numIslands(char[][] grid) {
        if(grid.length == 0) {
            return 0;
        }
        
        int rc = grid.length;
        int cc = grid[0].length;
        
        int islands = 0;
        
        for(int r = 0; r < rc; r++) {
            for(int c = 0; c < cc; c++) {
                if(grid[r][c] == '1') {
                    islands += 1;
                    dfs(grid, r, c);
                }
            }
        }
        return islands;
    }
}