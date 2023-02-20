class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        nums = [2, 3, 5]
        for num in nums:
            while n % num == 0:
                n = n // num
        return True if n == 1 else False
        