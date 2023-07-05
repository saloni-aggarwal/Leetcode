class Solution:
    def countOnes(self, nums, n, longest):
        i = 0
        while i < n:
            temp = 0
            while i < n and nums[i] == 1:
                temp += 1
                i += 1
            longest = max(longest, temp)
            i += 1
        return longest
                
    def longestSubarray(self, nums: List[int]) -> int:        
        n = len(nums)
        longest = self.countOnes(nums, n, 0)  
        if longest == n:
            return n-1
        for i in range(n):
            if nums[i] == 0:
                longest = max(longest, self.countOnes(nums[:i] + nums[i+1:], n-1, longest))
        return longest