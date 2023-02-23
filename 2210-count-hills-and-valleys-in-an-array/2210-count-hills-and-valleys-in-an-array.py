class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        idx = 1
        while idx < len(nums) and nums[idx] == nums[idx-1]:
            idx += 1
        if idx == len(nums):
            return 0
        count = 0
        while idx < len(nums)-1:
            # print("idx =", idx)
            i, j = idx-1, idx+1
            while i >=0 and nums[idx] == nums[i]:
                # print("in while i =", i)
                i -= 1
            while j < len(nums) and nums[idx] == nums[j]:
                # print("in while j =", j)
                j += 1
            # print("i =", i, "j =", j)
            if i >=0 and j < len(nums):
                if nums[i] > nums[idx] and nums[j] > nums[idx]:
                    # print("in first if count =", count)
                    count += 1
                if i >=0 and j < len(nums) and nums[i] < nums[idx] and nums[j] < nums[idx]:
                    # print("in second if count =", count)
                    count += 1
            idx = j
        return count
            
        