class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx1, idx2 = 0, 0
        size1, size2 = len(s), len(t)
        while idx1 < size1 and idx2 < size2:
            if s[idx1] == t[idx2]:
                idx1 += 1
            idx2 += 1
        if idx1 == size1:
            return True
        else:
            return False
        