from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = [x for x in words[0]]
        if len(words) == 1:
            return s
        common = Counter(s)
        # for ch in words[0]:
        #     if ch in words[1]:
        #         common[ch] += 1
        # print(common)
        for i in range(1, len(words)):
            # print("words[i] =", words[i])
            # print("common =", common)
            letters = [x for x in words[i]]
            # print(letters)
            letters = Counter(letters)
            # print(letters)
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
        
        