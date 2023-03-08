class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            ch = name[i]
            cntI = cntJ = 0
            while i < len(name) and name[i] == ch:
                i += 1
                cntI += 1
            # print("i =", i)
            # print("cntI =", cntI)
            if ch != typed[j]:
                return False
            while j < len(typed) and typed[j] == ch:
                j += 1
                cntJ += 1
            # print("j =", j)
            # print("cntJ =", cntJ)
            if cntJ < cntI:
                return False
        if j < len(typed) or i < len(name):
            return False
        return True
            
            
        