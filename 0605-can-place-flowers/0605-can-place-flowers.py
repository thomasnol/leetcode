class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # lastemptycount: counts how many flowerbeds were empty
        # if lastemptycount == 3, we set it to 1 and n -= 1. if n == 0 we return true
        if n == 0:
            return True
        lastemptycount = 1
        for f in flowerbed:
            if f == 0:
                lastemptycount += 1
            else:
                lastemptycount = 0
            if lastemptycount == 3:
                lastemptycount = 1
                n -= 1
                if n <= 0:
                    return True
        if lastemptycount == 2:
            n -= 1
            if n <= 0:
                return True
        return False