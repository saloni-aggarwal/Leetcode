class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        stringMap = Counter(s)
        cnt = 0
        for i, ele in enumerate(stringMap):
            if i == 0:
                cnt = stringMap[ele]
            if stringMap[ele] != cnt:
                return False
        return True
            
        