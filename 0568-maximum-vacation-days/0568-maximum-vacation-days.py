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