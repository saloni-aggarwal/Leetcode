class Solution {
    public int findMin(int[] nums) {
        int i = 0, j = nums.length-1;
        int mid;
        while(i < j) {
            
            mid = (i + j) / 2;
            if(nums[i] < nums[j])
                return nums[i];
            else {
                if (nums[mid]<nums[j]){
                    i++;
                    j = mid;
                }
                else {
                    i = mid+1;
                }
            }
        }
        return nums[i];
        
    }
}