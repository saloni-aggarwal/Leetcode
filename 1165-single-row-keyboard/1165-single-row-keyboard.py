class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        i, total = 0, 0
        
        for ch in word:
            j = keyboard.index(ch)
            total += abs(i-j)
            i = j
            
        return total
        