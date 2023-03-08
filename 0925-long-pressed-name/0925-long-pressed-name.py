class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        
        while i < len(name) and j < len(typed):            
            ch = name[i]
            cnt = 0
            
            while i < len(name) and name[i] == ch:
                i += 1
                cnt += 1
                
            if ch != typed[j]:
                return False
            
            while j < len(typed) and typed[j] == ch:
                j += 1
                cnt -= 1
                
            if cnt > 0:
                return False
            
        if j < len(typed) or i < len(name):
            return False
        
        return True
            
            
        