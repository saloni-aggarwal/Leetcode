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
            for(int j = 0; j < n; j++) {
                if(i == 0 || i == m-1 || j == 0 || j == n-1) {
                    if(grid[i][j] == 1)
                        dfs(grid, i, j, m, n);
                }
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