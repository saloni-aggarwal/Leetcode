class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        total = 0
        for ch in countT:
            if ch not in countS:
                total += countT[ch]
            else:
                if countT[ch] - countS[ch] > 0:
                    total += (countT[ch] - countS[ch])
        return total