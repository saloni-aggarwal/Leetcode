class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 1
        while i < len(nums) and nums[i] == nums[i-1]:
            i += 1
        if i == len(nums):
            return True
        isIncreasing = False if nums[i] - nums[i-1] < 0 else True
        for i in range(1, len(nums)-1):
            if isIncreasing and nums[i+1] - nums[i] < 0:
                return False
            elif not isIncreasing and nums[i+1] - nums[i] > 0:
                return False
        return True
        
        