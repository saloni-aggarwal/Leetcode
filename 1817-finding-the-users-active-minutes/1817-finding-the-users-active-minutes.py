from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uniqueLog = defaultdict(set)
        for log in logs:
            uniqueLog[log[0]].add(log[1])
        
        res = [0] * k
        for user in uniqueLog:
            n = len(uniqueLog[user])
            res[n-1] += 1
        return res
        