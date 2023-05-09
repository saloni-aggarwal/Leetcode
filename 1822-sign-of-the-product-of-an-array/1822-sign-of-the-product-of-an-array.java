class Solution {
    public int arraySign(int[] nums) {
        int totalNeg = 0;
        boolean isZero = false;
        
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] < 0) {
                totalNeg += 1;
            }
            else if(nums[i] == 0) {
                isZero = true;
            }
        }
        
        if(isZero) 
            return 0;
        else if(totalNeg % 2 != 0)
            return -1;
        else
            return 1;
        
    }
}