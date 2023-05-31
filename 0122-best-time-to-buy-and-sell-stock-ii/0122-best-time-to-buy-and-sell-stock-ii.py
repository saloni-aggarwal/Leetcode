class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMin = localMax = prices[0]
        total = 0
        
        for i in range(1, len(prices)):
            if prices[i] < localMax:
                total += (localMax - localMin)
                localMin = prices[i]
            localMax = prices[i]
            
        total += (localMax - localMin)
            
        return total
        