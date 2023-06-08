class Solution {
    public int countNegatives(int[][] grid) {
        int total = 0;
        int n = grid[0].length;
        for(int[] row: grid) {
            // for(int j = grid[0].length-1; j >= 0 ; j--) {
            //     if(grid[i][j] >= 0) {
            //         break;
            //     }
            //     total += 1;
            // }
            int i = 0, j = n-1;
            while(i <= j) {
                int mid = (i + j) / 2;
                if(row[mid] < 0) {
                    j = mid - 1;
                } else {
                    i = mid + 1;
                }
            }
            total += (n - i);
        }
        return total;
        
    }
}