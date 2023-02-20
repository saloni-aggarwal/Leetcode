class Solution:
    def minPartitions(self, n: str) -> int:
        val = float('-inf')
        for s in n:
            val = max(val, int(s))
            
        return val
            