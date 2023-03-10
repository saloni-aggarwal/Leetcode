class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[0] = cost[0]
        for i in range(1, len(dp)):            
            if i == len(dp)-1:
                dp[i] = min(dp[i-1], dp[i-2])
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
                
        return dp[-1] 
        