class Solution:
    def arrangeCoins(self, n: int) -> int:
        flag = True
        i = 1
        counter = 0
        while flag:
            if n - i < 0:
                return counter
            n -= i
            i += 1
            counter += 1
        