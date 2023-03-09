class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # print("cost =", cost)
        dp = [0] * (len(cost)+1)
        for i in range(0, len(dp)):
            
            if i == 0:
                dp[i] = cost[i]
            
            elif i == len(dp)-1:
                # print("in elif")
                dp[i] = min(dp[i-1], dp[i-2])
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            # print("dp =", dp)
            # print("i =", i)
        return dp[-1] 
        