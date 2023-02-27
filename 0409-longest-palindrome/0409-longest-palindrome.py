from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        stringMap = Counter(s)
        eventotal = 0
        oddtotal = 0
        isOdd = False
        for st in stringMap:
            if stringMap[st] % 2 == 0:
                eventotal += stringMap[st]
            else:
                oddtotal += stringMap[st] - 1
                isOdd = True
        if oddtotal == 0 and not isOdd:
            return eventotal      
        # elif eventotal == 0:
        #     return oddtotal + 1
        else:
            return oddtotal + eventotal + 1
        