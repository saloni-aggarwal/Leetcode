class Solution:
    def sortSentence(self, s: str) -> str:
        wordList = s.split()
        words = [""] * len(wordList)
        for word in wordList:
            idx = int(word[-1])
            words[idx-1] = word[:len(word)-1]
            
        return ' '.join(words)