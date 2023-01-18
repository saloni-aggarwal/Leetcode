class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        for i in range(len(pref)):
            if i == 0:
                res.append(pref[i])
            else:
                res.append(pref[i] ^ pref[i-1])
        return res