# # Solution 1 (top down approach)
# class Solution:
#     def dp(self, start, n, s, memo, dictionary):
#         if start == n:
#             return 0
#         elif memo[start] != -1:
#             return memo[start]
        
#         ans = self.dp(start+1, n, s, memo, dictionary) + 1
        
#         for end in range(start, n):
#             subStr = s[start : end+1]
#             if subStr in dictionary:
#                 ans = min(ans, self.dp(end+1, n, s, memo, dictionary))
        
#         memo[start] = ans
#         return ans
    
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         n = len(s)
#         memo = [-1] * n
#         return self.dp(0, n, s, memo, dictionary)
    

# Solution 2
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n+1)
        
        for start in range(n-1, -1, -1):
            dp[start] = dp[start+1] + 1
            for end in range(start, n):
                subStr = s[start:end+1]
                if subStr in dictionary:
                    dp[start] = min(dp[start], dp[end+1])
        
        return dp[0]
                