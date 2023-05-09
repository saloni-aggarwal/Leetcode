class Solution {
    public int diagonalSum(int[][] mat) {
        int total = 0;
        int n = mat.length;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(i == j) 
                    total += mat[i][j];
                else if((i + j) == n-1) 
                    total += mat[i][j];
            }
        }
        return total;
        
    }
}