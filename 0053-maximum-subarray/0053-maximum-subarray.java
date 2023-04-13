class Solution {
    public int maxSubArray(int[] nums) {
        // int[] dp = new int[nums.length];
        int ans = nums[nums.length-1];
        // dp[nums.length-1] = ans = nums[nums.length-1];
        for(int i = nums.length-2; i >= 0; i--) {
            nums[i] = Math.max(nums[i], nums[i]+nums[i+1]);
            ans = Math.max(ans, nums[i]);
        }
        
        return ans;
        
    }
}