class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        end = total = 0
        for i in range(len(timeSeries)):
            if i > 0 and end > timeSeries[i]:
                total += (timeSeries[i] - timeSeries[i-1])
            else:
                total += duration
            end = timeSeries[i] + duration
        return total
            
        