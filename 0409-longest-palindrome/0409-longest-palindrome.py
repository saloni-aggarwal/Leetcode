from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        stringMap = Counter(s)
        maxOdd = 0
        eventotal = 0
        oddtotal = 0
        isOdd = False
        for st in stringMap:
            if stringMap[st] % 2 == 0:
                eventotal += stringMap[st]
            else:
                oddtotal += stringMap[st] - 1
                isOdd = True
        if oddtotal == 0:
            if isOdd:
                return eventotal + 1
            else:
                return eventotal        
        elif eventotal == 0:
            return oddtotal + 1
        else:
            return oddtotal + eventotal + 1
        