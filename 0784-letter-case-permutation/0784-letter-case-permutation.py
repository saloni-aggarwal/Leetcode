class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = set()
        
        def recur(s, idx, n):
            if idx == n:
                ans.add(s)
                return
            
            if s[idx].isalpha():
                recur(s[:idx]+s[idx].lower()+s[idx+1:], idx+1, n)
                recur(s[:idx]+s[idx].upper()+s[idx+1:], idx+1, n)
            else:
                recur(s, idx+1, n)
        
        recur(s, 0, len(s))
        return ans