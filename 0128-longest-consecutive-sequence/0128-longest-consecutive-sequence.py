class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put all elements in set
        # go through entire set
        # example set: 0,1,2,4
        # goal is to locate 0 (such that n-1 doesn't exist)
        # then keep checking for n+1, updating n
        # turns out you can do this for entire set, keeping a longest and doing max
        elements = set(nums)
        longest = 0
        for e in elements:
            if (e - 1) not in elements:
                streak = 1
                # longest = max(longest, streak)
                while (e + 1) in elements:
                    e += 1
                    streak += 1
                longest = max(longest, streak)
        return longest