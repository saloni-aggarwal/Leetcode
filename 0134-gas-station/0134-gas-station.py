class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         Solution 1 - TLE (44/50)
        
#         diff = []
#         n = len(cost)
#         for i in range(n):
#             diff.append(gas[i] - cost[i])
            
#         if sum(diff) < 0:
#             return -1
        
#         for i, d in enumerate(diff):
#             if d >= 0:
#                 start = (i + 1) % n
#                 pos = d
#                 while start != i and pos >= 0:
#                     pos += diff[start]
#                     start = (start + 1) % (n)
#                 if start == i:
#                     return i
            
#         return -1

#         Solution 2
        totalCost = currCost = ans = 0 
        
        for i in range(len(gas)):
            totalCost += (gas[i] - cost[i])
            currCost += (gas[i] - cost[i])
            
            if currCost < 0:
                ans = i + 1
                currCost = 0
                
        return ans if totalCost >= 0 else -1