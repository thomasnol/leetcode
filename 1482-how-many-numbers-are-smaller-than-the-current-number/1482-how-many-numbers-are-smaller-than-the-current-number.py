class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # similar to 2 sum, the key here is to do all the calculations a sorted version of the list. then use the data to get the answer for the original list
        # map values to answer: [1,2,2,3,8]
        sorted_nums = sorted(nums)
        nums_to_answer = {}
        for i, n in enumerate(sorted_nums):
            if n not in nums_to_answer:
                nums_to_answer[n] = i
        res = []
        for n in nums:
            res.append(nums_to_answer[n])
        return res