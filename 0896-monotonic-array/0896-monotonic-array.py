class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        j = 1
        while j < len(nums) and nums[j] == nums[j-1]:
            j += 1
        if j == len(nums):
            return True
            
        isIncreasing = False if nums[j] - nums[j-1] < 0 else True
        for i in range(1, len(nums)-1):
            if isIncreasing and nums[i+1] - nums[i] < 0:
                return False
            elif not isIncreasing and nums[i+1] - nums[i] > 0:
                return False
        return True
        
        