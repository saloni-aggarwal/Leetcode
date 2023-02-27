from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # print("length =", len(s))
        stringMap = defaultdict(int)
        for st in s:
            stringMap[st] += 1
        print(stringMap)
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
            # print("total =", total)
        # oddtotal -= (maxOdd - 1)
        print("oddtotal =", oddtotal)
        print("eventotal =", eventotal)
        if oddtotal == 0:
            if isOdd:
                return eventotal + 1
            else:
                return eventotal        
        elif eventotal == 0:
            return oddtotal + 1
        else:
            return oddtotal + eventotal + 1
        