class Solution {
    
    public int diagonalPrime(int[][] nums) {
        Set<Integer> diagnols = new HashSet<>();
        int n = nums.length;
        int m = nums[0]. length;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if (i == j) {
                    diagnols.add(nums[i][j]);
                } else if ((i + j) == Math.min(n,m)-1) {
                    diagnols.add(nums[i][j]);
                }
            }
        }
        int maxVal = 0;
        for(int num: diagnols)  {
            // System.out.println(num);
            if(isPrime(num)) 
                maxVal = Math.max(maxVal, num);
        }
        
        return maxVal;
    }
    
    public boolean isPrime(int num) {
        if (num < 2) 
            return false;
        for(int j = 2; j <= Math.sqrt(num); j++) {
            if(num % j == 0) {
                return false;
            }
        }
        return true;
    }
}