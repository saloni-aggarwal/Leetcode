class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        
        for note in ransomNote:
            if available[note] == 0:
                return False
            available[note] -= 1
        
        return True