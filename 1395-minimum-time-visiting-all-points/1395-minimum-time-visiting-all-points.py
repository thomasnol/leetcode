class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curx, cury = points[0][0], points[0][1]
        d = 0
        for p in points[1:]:
            dx = abs(curx - p[0])
            dy = abs(cury - p[1])
            d += max(dx, dy)
            curx, cury = p[0], p[1]
        return d