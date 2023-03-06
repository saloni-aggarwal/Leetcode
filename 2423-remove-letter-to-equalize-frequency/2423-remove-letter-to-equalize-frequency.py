class Solution:
    
    def check(self, word):
        chFreq = Counter(word)
        uniqueFreq = set(chFreq.values())
        if len(uniqueFreq) == 1:
            return True
        return False
            
    def equalFrequency(self, word: str) -> bool:
        chFreq = Counter(word)
        if len(chFreq) == 1:
            return True
        uniqueFreq = set(chFreq.values())
        # print(uniqueFreq, uniqueFreq[0])
        if len(uniqueFreq) == 1:
            if uniqueFreq.pop() == 1:
                return True
            else:
                return False
        for i in range(len(word)):
            if self.check(word[:i] + word[i+1:]):
                return True
        return False
                    