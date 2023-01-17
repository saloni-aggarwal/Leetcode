from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastInd = defaultdict(int)

        for i, ch in enumerate(s):
            lastInd[ch] = i

        lastVal = 0
        j = 0
        ans = []

        for i, ch in enumerate(s):
            j = max(j, lastInd[ch])
            if i == j:
                ans.append(i - lastVal + 1)
                lastVal = i + 1
        return ans