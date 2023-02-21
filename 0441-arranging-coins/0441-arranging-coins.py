class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while True:
            if n - i < 0:
                return i-1
            n -= i
            i += 1
        