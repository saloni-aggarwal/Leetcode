class Solution:
    def sortSentence(self, s: str) -> str:
        
#         APPROACH 1
        # wordList = s.split()
        # words = [""] * len(wordList)
        # for word in wordList:
        #     idx = int(word[-1])
        #     words[idx-1] = word[:len(word)-1]
        
#         APPROACH 2
    
        words = [""] * len(s.split())
        word = ""
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i].isdigit():
                words[int(s[i])-1] = word
                i += 1
                word = ""
            else:
                word += s[i]
            
            
        return ' '.join(words)