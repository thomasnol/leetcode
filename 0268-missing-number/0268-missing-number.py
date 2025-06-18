class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        psnums = set(nums)
        for i in range(len(nums) + 1):
            if i not in psnums:
                return i