class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        # print("first =", first, "second =", second, "third =", third)
        ans = []
        for word in words:
            w = set(word.lower())
            f = s = t = True
            # print("w =", w)
            for ch in w:
                # print("ch =", ch)
                if ch not in first:
                    f = False
                if ch not in second:
                    s = False
                if ch not in third:
                    t = False
            # print("f =", f, "s =", s, "t =", t)
            if f or s or t:
                ans.append(word)
        return ans
            
        