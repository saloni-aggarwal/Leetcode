class Solution {
    public int diagonalSum(int[][] mat) {
        int total = 0;
        int n = mat.length;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(i == j) {
                    // System.out.println("first if mat[i][j] = " + mat[i][j]);
                    total += mat[i][j];
                } 
                else if((i + j) == n-1) {
                    // System.out.println("second if mat[i][j] = " + mat[i][j]);
                    total += mat[i][j];
                }
                // System.out.println("total = " + total);
            }
        }
        // if(n%2 != 0 && n != 1) {
        //     total -= mat[n/2][n/2];
        // }
        return total;
        
    }
}