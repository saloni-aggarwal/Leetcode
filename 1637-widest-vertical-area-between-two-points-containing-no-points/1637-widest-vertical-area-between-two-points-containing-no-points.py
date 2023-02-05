class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[0])
        j = 1
        res = 0
        while j < len(points):
            res = max(res, points[j][0]-points[j-1][0])
            j += 1
        return res
        