class Solution:
    
    def check(self, word):
        chFreq = Counter(word)
        uniqueFreq = set(chFreq.values())
        if len(uniqueFreq) == 1:
            return True
        return False
            
    def equalFrequency(self, word: str) -> bool:        

        for i in range(len(word)):
            if self.check(word[:i] + word[i+1:]):
                return True
        return False
                    