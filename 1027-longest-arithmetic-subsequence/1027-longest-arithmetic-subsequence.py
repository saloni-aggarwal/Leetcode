from collections import defaultdict
class Solution:
        
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [defaultdict(int) for _ in range(n)]
        
        for r in range(1,n):
            for l in range(r):
                diff = nums[r] - nums[l]
                dp[r][diff] = dp[l].get(diff,1)+1
                ans = max(ans, dp[r][diff])

        return ans