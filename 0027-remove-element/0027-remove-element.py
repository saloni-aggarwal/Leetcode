class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        
        while i < j:
            
            nums[i], nums[j] = nums[j], nums[i]
            while j > i and nums[j] == val:
                j -= 1
                
            while i <= j and nums[i] != val:
                i += 1
                
        if i == j:
            if nums[i] != val:
                i += 1
            
            
        return i
        