class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n^2) solution:
        # go left to right, whenever an invalid digit is found, go to the right until end of array or a larger digit is found. once it's found, overwrite current invalid digit with new digit value. and make new digit value be invalid digit - 1.
        # if when going right, the new digit is smaller, treat it as an invalid digit, swapping it.

        # O(n) solution:
        # 2 sweeps?:
        # first sweep clears all invalid digits:
        # firstnum, secondnum are ints...
        # second sweep left aligns entire array:
        # not sure how to do this in O(n) without extra space.
        # 2 pointers? first pointer is for left-most cleared digit, second pointer is for left-most uncleared digit, when second > first.
        # this is probably overengineered though...

        invalid = (-10)**5
        n = len(nums)
        invalid_count = 0
        curr = nums[0]
        counter = 0
        for i in range(n):
            if nums[i] == curr:
                counter +=1
            else:
                counter = 1
                curr = nums[i]
            if counter >= 3:
                nums[i] = invalid
                invalid_count += 1
        
        left = 0
        for right in range(n):
            while left < right and nums[left] != invalid:
                left +=1 
            if nums[right] == invalid:
                continue
            nums[left], nums[right] = nums[right], nums[left]
    
        return n - invalid_count