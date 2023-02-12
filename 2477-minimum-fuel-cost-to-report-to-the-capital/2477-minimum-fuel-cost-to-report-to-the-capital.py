from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        
        for city1, city2 in roads:
            graph[city1].append(city2)
            graph[city2].append(city1)
        
        res = 0
            
        def dfs(curr, parent):
            
            nonlocal res
            
            totalPeople = 1
            
            for nei in graph[curr]:
                if nei != parent:
                    people, car = dfs(nei, curr)
                    
                    totalPeople += people
                    
                    res += car
                    
            cars = ceil(totalPeople/seats)
            
            return totalPeople, cars
        
        dfs(0, None)
        return res
                    
            
            
            
            