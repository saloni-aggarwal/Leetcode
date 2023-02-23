class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        idx = 1
        while idx < len(nums) and nums[idx] == nums[idx-1]:
            idx += 1
        if idx == len(nums):
            return 0
        count = 0
        while idx < len(nums)-1:
            i, j = idx-1, idx+1
            while i >=0 and nums[idx] == nums[i]:
                i -= 1
            while j < len(nums) and nums[idx] == nums[j]:
                j += 1
            if i >=0 and j < len(nums):
                if nums[i] > nums[idx] and nums[j] > nums[idx]:
                    count += 1
                if nums[i] < nums[idx] and nums[j] < nums[idx]:
                    count += 1
            idx = j
        return count
            
        