from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if nums.size() == 0: return 0
        # if nums.size() == 1: return nums[0]
        # return max between 2 options of robbing: either robber robbed current house or they didn't
        # return max(nums[-1] + rob(nums[:-2]),
                    # rob(nums[:-1]))
        
        @lru_cache
        def f(i):
            # if len(nums) == 0: return 0
            # if len(nums) == 1: return nums[0]
            if i >= len(nums):
                return 0
            
            rob = nums[i] + f(i+2)
            not_rob = f(i+1)

            return max(rob, not_rob)

        return f(0)