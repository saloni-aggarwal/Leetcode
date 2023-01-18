class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = [1] * 5
        for _ in range(n):
            for i in range(3,-1,-1):
                ans[i] += ans[i+1]
        return ans[0]