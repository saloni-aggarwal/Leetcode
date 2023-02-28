class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        lst = []
        for i in range(len(s)):
            if s[i] not in lst:
                lst.append(s[i])
                if i == len(s)-1:
                    return max(ans, len(lst))                
            else:
                ans = max(ans, len(lst))
                ind = lst.index(s[i])
                lst = lst[ind+1:]
                lst.append(s[i])
        return ans
        