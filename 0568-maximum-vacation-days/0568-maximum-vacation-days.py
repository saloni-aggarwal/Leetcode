# Solution 1

# class Solution:
    
#     def dfs(self, flights, days, curr_city, weekNo, n, k, memo):
#         if weekNo == k:
#             return 0
        
#         if memo[curr_city][weekNo]:
#             return memo[curr_city][weekNo]
        
#         maxVacDay = 0
#         for i in range(n):
#             if i == curr_city or flights[curr_city][i] == 1:
#                 vacationDays = days[i][weekNo] + self.dfs(flights, days, i, weekNo+1, n, k, memo)
#                 maxVacDay = max(maxVacDay, vacationDays)
                
#         memo[curr_city][weekNo] = maxVacDay        
#         return maxVacDay  
        
#     def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
#         n = len(flights)
#         k = len(days[0])
        
#         memo = [[None] * k] * n 
        
#         return self.dfs(flights, days, 0, 0, n, k, memo)


# Solution 2
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        cities = len(days)
        weeks = len(days[0])
        
        dp = []
        for i in range(cities):
            temp = [0 for _ in range(weeks+1)]
            dp.append(temp)
            
        
        for  i in range(weeks-1, -1, -1):
            for currCity in range(cities):
                dp[currCity][i] = days[currCity][i] + dp[currCity][i+1]
                for neighbourCity in range(cities):
                    if flights[currCity][neighbourCity] == 1:
                        dp[currCity][i] = max(days[neighbourCity][i] + dp[neighbourCity][i+1], dp[currCity][i])
                        
        return dp[0][0]