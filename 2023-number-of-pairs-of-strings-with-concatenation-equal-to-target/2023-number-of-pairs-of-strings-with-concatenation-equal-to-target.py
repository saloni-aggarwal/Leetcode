from collections import defaultdict
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    word = nums[i] + nums[j]
                    if word == target:
                        count += 1
                    
        return count
                    