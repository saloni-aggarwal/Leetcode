from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityMap = defaultdict(list)
        for path in paths:
            cityMap[path[0]].append(path[1])
        # print("cityMap =", cityMap)
        for path in paths:
            # print("city =", city)
            # print("cityMap[city]", cityMap[city])
            if path[1] not in cityMap:
                return path[1]
        return ""
            