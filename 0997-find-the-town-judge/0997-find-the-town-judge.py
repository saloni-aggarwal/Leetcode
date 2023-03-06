from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustOn = [0] * n
        trustTo = [0] * n
        
        for a, b in trust:
            trustOn[b-1] += 1
            trustTo[a-1] += 1
        for i in range(n):
            if trustOn[i] == n-1 and trustTo[i] == 0:
                return i+1
        return -1
            
        
        