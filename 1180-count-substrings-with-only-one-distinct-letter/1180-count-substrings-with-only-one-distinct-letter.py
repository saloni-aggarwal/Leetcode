class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        right, left = 0, 0
        
        while right < len(s):
            while right < len(s) and s[right] == s[left]:
                right += 1
            subStr = right - left
            total += (1 + subStr) * subStr // 2
            left = right
            
        return total