class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, result = 0, 0
        
        for num in nums:
            total += num
            result += 1
            if total >= target:
                break
            
        if total < target:
            return 0
        
        prevCurr = result
        
        for i in range(1, len(nums)):
            total -= nums[i-1]
            curr = prevCurr - 1
            
            while total < target and i + curr < len(nums):
                total += nums[i+curr]
                curr += 1
            
            prevCurr = curr
            
            if total < target:
                return result
            else:
                result = min(result, curr)
                
        return result