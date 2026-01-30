class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort potions by increasing order
        # go through spells array
        # for each spell:
        # check if product is success. if not, try next potion
        # if it is, add X successes and move to next spell.
        # X is just how many remaining potions + 1 or such
        potions.sort()
        res = []
        for s in spells:
            target = (success + s - 1) // s
            # (10 + 3 - 1) // 3
            # (13 - 1) // 3
            res.append(0)
            left = 0
            right = len(potions) - 1
            if potions[right] < target:
                continue
            while left < right:
                cur = left + (right - left) // 2
                # cur = (left + right) // 2
                if potions[cur] >= target:
                    right = cur
                    # print("s:", s)
                    # print("p:", p)
                    # print("i:", i)
                else:
                    left = cur + 1
            res[-1] = len(potions) - left
            # break
        return res