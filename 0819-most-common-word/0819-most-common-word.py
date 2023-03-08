from collections import defaultdict
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower().replace(',', ' ')
        paragraph = paragraph.translate(str.maketrans(' ',' ',string.punctuation))
        print(paragraph)
        wordArr = paragraph.split()
        # print(wordArr)
        wordCounter = defaultdict(int)
        for word in wordArr:
            wordCounter[word] += 1
        # print(wordCounter)
        maxCnt = float('-inf')
        maxWord = ""
        
        for word in wordArr:
            if (word not in banned) and wordCounter[word] > maxCnt:
                maxCnt = wordCounter[word]
                maxWord = word
        return maxWord