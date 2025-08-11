from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # have a dp array that has rob up to i ?
        # dp = [0] * len(nums)
        # dp[0] = 


































        @lru_cache
        def f(i):
            if i >= len(nums):
                return 0
            
            rob = nums[i] + f(i+2)
            not_rob = f(i+1)

            return max(rob, not_rob)

        return f(0)