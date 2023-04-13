class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        arr = [0] * 26
        beg, maxLen, largestCnt = 0,0,0
        for end in range(len(s)):
            arr[ord(s[end]) - ord('A')] += 1
            largestCnt = max(largestCnt, arr[ord(s[end]) - ord('A')])
            
            if (end - beg + 1 - largestCnt) > k:
                arr[ord(s[beg]) - ord('A')] -= 1
                beg += 1
            
            maxLen = max(maxLen, (end-beg+1))
            
        return maxLen
        