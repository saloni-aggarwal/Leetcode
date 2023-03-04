class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        total = 0
        for ch in countT:
            if ch not in countS:
                total += countT[ch]
            else:
                # :
                total += (countT[ch] - countS[ch]) if countT[ch] - countS[ch] > 0 else 0
        return total