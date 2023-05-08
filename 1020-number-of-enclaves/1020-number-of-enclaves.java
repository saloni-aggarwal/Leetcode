class Solution {
    public void dfs(int[][] grid, int i, int j, int m, int n) {
        if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0)
            return;
        
        grid[i][j] = 0;
        
        int[][] dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        
        for(int[] dir: dirs) {
            dfs(grid, i+dir[0], j+dir[1], m, n);
        }
    }
    
    public int numEnclaves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        for(int i = 0; i < m; i++) {
            if(grid[i][0] == 1) {
                dfs(grid, i, 0, m, n);
            }
        }
        
        for(int i = 0; i < m; i++) {
            if(grid[i][n-1] == 1) {
                dfs(grid, i, n-1, m, n);
            }
        }
        
        for(int i = 0; i < n; i++) {
            if(grid[0][i] == 1) {
                dfs(grid, 0, i, m, n);
            }
        }
        
        for(int i = 0; i < n; i++) {
            if(grid[m-1][i] == 1) {
                dfs(grid, m-1, i, m, n);
            }
        }
                
        int count = 0;
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    count++;
                }
            }
        }
        
        return count;
    }
}