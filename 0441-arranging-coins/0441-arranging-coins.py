class Solution:
    def arrangeCoins(self, n: int) -> int:
        flag = True
        i = 1
        while flag:
            if n - i < 0:
                return i-1
            n -= i
            i += 1
        