from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # base cases are when have 0 or 1 houses left
        # location is current index
        loc = 0
        mapping = {}
        
        def f(loc):
            if loc + 1 == len(nums):
                mapping[loc] = nums[loc]
                return nums[loc]
            if loc + 1 > len(nums):
                mapping[loc] = 0
                return 0
            if loc in mapping:
                return mapping[loc]
            rob = nums[loc] + f(loc + 2)
            not_rob = f(loc + 1)
            res = max(rob, not_rob)
            mapping[loc] = res
            return res
        
        return f(0)































        # @cache
        # @lru_cache
        lookup = {}
        # i is the index of the house ur at
        def f(i):
            if i in lookup:
                return lookup[i]
            
            if i >= len(nums):
                return 0
            
            rob = nums[i] + f(i+2)
            not_rob = f(i+1)

            lookup[i] = max(rob, not_rob)

            return max(rob, not_rob)

        return f(0)