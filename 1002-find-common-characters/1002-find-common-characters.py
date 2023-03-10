from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = [x for x in words[0]]
        if len(words) == 1:
            return s
        common = Counter(s)
        
        for i in range(1, len(words)):
            letters = [x for x in words[i]]
            letters = Counter(letters)
            for ch in common:
                if common[ch] != 0:
                    if ch not in letters:
                        common[ch] == 0
                    if letters[ch] < common[ch]:
                        common[ch] = letters[ch]
                        
        ans = []        
        for ch in common:
            if common[ch] != 0:
                ans.extend(ch * common[ch])
        return ans
        
        