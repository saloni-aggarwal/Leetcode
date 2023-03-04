class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # i, j = 0, len(nums)-1
        # total 
        mult1 = nums[0] * nums[1] * nums[-1]
        mult2 = nums[-1] * nums[-2] * nums[-3]
        return max(mult1, mult2)
