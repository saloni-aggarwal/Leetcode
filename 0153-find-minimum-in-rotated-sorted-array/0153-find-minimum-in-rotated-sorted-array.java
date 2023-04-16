class Solution {
    public int findMin(int[] nums) {
        int i = 0, j = nums.length-1;
        int mid;
        while(i < j) {
            mid = (i + j) / 2;
            if(nums[i] < nums[j])
                j = mid;
            else {
                if (nums[mid]<nums[j]){
                    i++;
                    j = mid;
                }
                else {
                    i = mid+1;
                }
                
                // ans = Math.min(ans, nums[i]);
            }
        }
        return nums[i];
        
    }
}