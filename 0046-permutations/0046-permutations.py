class Solution:
    def __init__(self):
        self.ans = []
        
    def backtrack(self, nums, curr):
        if len(curr) == len(nums):
            self.ans.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                self.backtrack(nums, curr)
                curr.pop()
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.ans
        