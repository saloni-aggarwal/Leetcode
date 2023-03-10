class Solution:
    def digitCount(self, num: str) -> bool:
        numCnt = Counter(num)
        for i in range(len(num)):
            if numCnt[str(i)] != int(num[i]):
                return False
        return True
                
            
            
        
        