class Solution:
    def isArmstrong(self, n: int) -> bool:
        temp = n
        total, k = 0, 0
        
        while temp > 0:
            temp //= 10
            k += 1
        
        temp = n
        
        while temp > 0:
            rem = temp % 10
            temp //= 10
            total += rem ** k
            
        return total == n