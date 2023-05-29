from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
        k = 0
        
        for c in count:
            t = min(2, count.get(c))
            for _ in range(t):
                nums[k] = c
                k += 1
            
        return k
        
        