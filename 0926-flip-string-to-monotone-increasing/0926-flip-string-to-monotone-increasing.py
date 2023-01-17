class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans, num = 0, 0
        for ch in s:
            if ch == '0':
                ans = min(num, ans+1)
            else:
                num += 1
        return ans
        