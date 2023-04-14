class Solution {
    public int maxProduct(int[] nums) {
        int ans = nums[0], maxVal = nums[0], minVal = nums[0];
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] >= 0) {
                maxVal = Math.max(nums[i], nums[i] * maxVal);
                minVal = Math.min(nums[i], nums[i] * minVal);
            } else {
                int t = maxVal;
                maxVal = Math.max(nums[i], nums[i] * minVal);
                minVal = Math.min(nums[i], nums[i] * t);
            }
            // System.out.println("maxVal = " +maxVal);
            // System.out.println("minVal = " +minVal);
            ans = Math.max(ans, maxVal);
            // System.out.println("ans = " + ans);
        }
        return ans;
    }
}