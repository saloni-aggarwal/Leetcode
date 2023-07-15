class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        wordToLetter = collections.defaultdict(str)
        letterToWord = collections.defaultdict(str)
        
        for i in range(len(pattern)):
            if pattern[i] not in letterToWord and s[i] not in wordToLetter:
                letterToWord[pattern[i]] = s[i]
                wordToLetter[s[i]] = pattern[i]
            
            else:
                if letterToWord[pattern[i]] != s[i]:
                    return False
        return True
            