class Solution:
    def isValid(self, s: str) -> bool:
        openCloseMap = {"(" : ")", "{" : "}", "[" : "]"}
        
        if not s or len(s) < 2:
            return False
        
        stack = deque()
        for st in s:
            if st in openCloseMap.keys():
                stack.append(st)
            elif stack and openCloseMap[stack[-1]] == st :
                stack.pop()
            else:
                return False
            
        if stack:
            return False
        return True