class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = nums[0]
        ans = []
        for j in range(len(nums)):
            if j+1 == len(nums) or nums[j]+1 != nums[j+1]:
                if start != nums[j]:
                    ans.append(str(start) + "->" + str(nums[j]))
                else:
                    ans.append(str(start))
                if j < len(nums)-1:
                    start = nums[j+1]
        return ans
            