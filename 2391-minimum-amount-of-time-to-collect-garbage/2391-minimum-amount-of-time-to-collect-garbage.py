from collections import Counter
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        garbageIdx = {'G':-1, 'M':-1, 'P':-1}
        count = {'G':0, 'M':0, 'P':0}
        
        for i in range(len(garbage)):
            cnt = Counter(garbage[i])
            for c in cnt:
                count[c] += cnt[c]
                garbageIdx[c] = i
        for i in range(len(travel)):
            if i == 0:
                continue
            else:
                travel[i] += travel[i-1]
                
        total = 0
        for typ in garbageIdx:
            if garbageIdx[typ] > 0:
                total += count[typ] + travel[garbageIdx[typ]-1]
            else:
                total += count[typ]
        return total
                
        
        