class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                i = j = mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i+1, j-1]
            elif nums[mid] > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]