class Solution {
    public int minimizeArrayValue(int[] nums) {
        long maxVal = 0;
        long sum = 0;
        
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i];
            maxVal = Math.max(maxVal, (sum + i) / (i+1));
        }
        return (int)maxVal;
    }
}