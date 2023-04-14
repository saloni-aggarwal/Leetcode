class Solution {
    public int climbStairs(int n) {
        int first = 1, second = 2;
        if(n == 1) {
            return first;
        } else if(n == 2) {
            return second;
        } else {
            for(int i = 3; i <= n; i++) {
                int temp = first;
                first = second;
                second += temp;
            }
        }
        return second;
        
    }
}