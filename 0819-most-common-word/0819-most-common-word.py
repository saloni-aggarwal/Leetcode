import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower().replace(',', ' ')
        paragraph = paragraph.translate(str.maketrans('','',string.punctuation))
        
        wordArr = paragraph.split()
        
        wordCounter = Counter(wordArr)
        
        maxCnt = float('-inf')
        maxWord = ""
        
        for word in wordArr:
            if (word not in banned) and wordCounter[word] > maxCnt:
                maxCnt = wordCounter[word]
                maxWord = word
        return maxWord