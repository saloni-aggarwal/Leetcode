class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        cnt  = 0
        for st in s:
            if st == 'R':
                r += 1
            elif st == 'L':
                l += 1
            if r == l:
                cnt += 1
        return cnt
        