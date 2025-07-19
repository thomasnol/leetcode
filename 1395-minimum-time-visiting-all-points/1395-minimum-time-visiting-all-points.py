class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curx = points[0][0]
        cury = points[0][1]
        d = 0
        for p in points[1:]:
            dx = abs(curx - p[0])
            dy = abs(cury - p[1])
            d += max(dx, dy)
            curx = p[0]
            cury = p[1]
        return d