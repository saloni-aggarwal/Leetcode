from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustOn = [0] * n
        trustFrom = [0] * n
        
        for a, b in trust:
            trustOn[b-1] += 1
            trustFrom[a-1] += 1
        for i in range(n):
            if trustOn[i] == n-1 and trustFrom[i] == 0:
                return i+1
        return -1
            
        
        