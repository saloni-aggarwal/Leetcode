class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        mid = (i + j) // 2     
        
        while i < j:
            print("i =", i, "j =", j)
            mid = (i + j) // 2
            print("mid =", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
                
        if target <= nums[i] :
            return i
        if target > nums[j]:
            return j + 1