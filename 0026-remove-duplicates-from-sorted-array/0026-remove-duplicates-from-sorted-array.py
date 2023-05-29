class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            
            j += 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
                
            i += 1
        
        return i