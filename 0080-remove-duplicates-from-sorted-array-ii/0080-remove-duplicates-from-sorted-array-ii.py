from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         Method 1
#         count = defaultdict(int)
        
#         for num in nums:
#             count[num] += 1
            
#         k = 0
        
#         for c in count:
#             t = min(2, count.get(c))
#             for _ in range(t):
#                 nums[k] = c
#                 k += 1
            
#         return k
        
        
#         Method 2

        i, count = 1, 1
    
        while i < len(nums):
            
            if nums[i] == nums[i-1]:
                count += 1
                
                if count > 2:
                    nums.pop(i)
                    i -= 1
                    
            else:
                count = 1
            
            i += 1
            
        return i
        