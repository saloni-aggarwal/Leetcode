class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        
        ans = []
        for word in words:
            w = set(word.lower())
            f = s = t = True
            for ch in w:
                if ch not in first:
                    f = False
                if ch not in second:
                    s = False
                if ch not in third:
                    t = False
            if f or s or t:
                ans.append(word)
                
        return ans
            
        