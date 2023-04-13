class Solution {
    public int maxSubArray(int[] nums) {
        int ans = nums[nums.length-1];
        for(int i = nums.length-2; i >= 0; i--) {
            nums[i] = Math.max(nums[i], nums[i]+nums[i+1]);
            ans = Math.max(ans, nums[i]);
        }
        
        return ans;
        
    }
}