from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityMap = defaultdict(list)
        for path in paths:
            cityMap[path[0]].append(path[1])
        for path in paths:
            if path[1] not in cityMap:
                return path[1]
        return ""
            