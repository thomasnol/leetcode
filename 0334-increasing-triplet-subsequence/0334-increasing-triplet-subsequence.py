class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # go through the array
        # goal is to keep the smallest possible first and second numbers, this gives the best chance of finding a valid third number
        fnum = float('inf')
        snum = float('inf')
        for n in nums:
            if n <= fnum:
                fnum = n
            elif n <= snum:
                # fnum = snum
                snum = n
            else:
                return True
        return False