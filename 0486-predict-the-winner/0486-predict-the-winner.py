class Solution:
    
    
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = collections.defaultdict(int)
        
        def findWinner(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            elif left == right:
                return nums[left]

            l = nums[left] - findWinner(left+1, right)
            r = nums[right] - findWinner(left, right-1)
            memo[(left, right)] = max(l, r)

            return memo[(left, right)]
        
        return findWinner(0, n-1) >= 0
        