class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        isjewel = set()
        res = 0
        for j in jewels:
            isjewel.add(j)
        for s in stones:
            if s in isjewel:
                res += 1
        return res