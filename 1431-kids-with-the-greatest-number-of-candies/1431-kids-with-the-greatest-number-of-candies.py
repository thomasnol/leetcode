class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        res = []
        for c in candies:
            if c + extraCandies >= maxcandies:
                res.append(True)
            else:
                res.append(False)
        return res