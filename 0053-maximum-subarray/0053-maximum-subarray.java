class Solution {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        int ans;
        dp[nums.length-1] = ans = nums[nums.length-1];
        for(int i = nums.length-2; i >= 0; i--) {
            dp[i] = Math.max(nums[i], nums[i]+dp[i+1]);
            ans = Math.max(ans, dp[i]);
        }
        
        return ans;
        
    }
}