class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map required number to index (for successful pair)
        pairn_to_index = {}
        for i, n in enumerate(nums):
            if n in pairn_to_index:
                return [i, pairn_to_index[n]]
            pairn_to_index[target - n] = i