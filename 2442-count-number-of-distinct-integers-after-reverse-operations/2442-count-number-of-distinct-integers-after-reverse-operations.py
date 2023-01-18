class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(num):
            out = 0
            while num >= 1:              
                out = (out * 10) + num%10
                num = num // 10
            return out
                
        n = len(nums)
        for i in range(n):
            # print(reverse(num))
            nums.append(reverse(nums[i]))
        return len(set(nums))
            
        