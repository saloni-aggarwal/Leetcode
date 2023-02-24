# from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set()
        for path in paths:
            src.add(path[0])
        for path in paths:
            if path[1] not in src:
                return path[1]
        return ""
            