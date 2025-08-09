class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        checkpoint = 0

        i = 0
        while i < len(nums) - 1 and nums[i] < nums[i+1]:
            i += 1
        if i == checkpoint:
            return False
        
        checkpoint = i
        while i < len(nums) - 1 and nums[i] > nums[i+1]:
            i += 1
        if i == checkpoint:
            return False
        
        checkpoint = i
        while i < len(nums) - 1 and nums[i] < nums[i+1]:
            i += 1
        if i == checkpoint:
            return False
        
        return i == len(nums) - 1


# class Solution:
#     def isTrionic(self, nums: list[int]) -> bool:
#         n = len(nums)
#         if n < 3:
#             return False
        
#         i = 0
        
#         # 1. strictly increasing
#         while i + 1 < n and nums[i] < nums[i+1]:
#             i += 1
#         if i == 0:  # No increase section
#             return False

#         # 2. strictly decreasing
#         j = i
#         while j + 1 < n and nums[j] > nums[j+1]:
#             j += 1
#         if j == i:  # No decrease section
#             return False
        
#         # 3. strictly increasing
#         k = j
#         while k + 1 < n and nums[k] < nums[k+1]:
#             k += 1
#         if k == j:  # No final increase section
#             return False

#         # Should have exhausted the list by now
#         return k == n - 1
