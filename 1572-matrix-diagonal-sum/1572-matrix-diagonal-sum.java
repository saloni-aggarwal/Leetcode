class Solution {
    public int diagonalSum(int[][] mat) {
        int total = 0;
        int n = mat.length;
        for(int i = 0; i < n; i++) {
            total += mat[i][i] + mat[i][n-i-1];
        }
        if(n%2 != 0) {
            total -= mat[n/2][n/2];
        }
        return total;
        
    }
}