class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # isjewel = set()
        # for j in jewels: isjewel.add(j)
        isjewel = set(jewels)
        for s in stones:
            if s in isjewel:
                res += 1
        return res