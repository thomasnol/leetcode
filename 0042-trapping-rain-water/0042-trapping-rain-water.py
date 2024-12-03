class Solution:
    def trap(self, height: List[int]) -> int:
        # for a given height[x]
        # find the max height from any nodes on the left
        # do the same for the nodes on the right
        # the trapped water in that column = min of both maximums - height[x]
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        count = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                # trap water in height[left]
                count += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                # trap water in height[right]
                count += right_max - height[right]
                right -= 1
        # better solution:
        # while left + 1 < right:
        #     if right_max > left_max:
        #         left += 1
        #         if height[left] > left_max:
        #             left_max = height[left]
        #         else:
        #             count += left_max - height[left]
        #     else:
        #         right -= 1
        #         if height[right] > right_max:
        #             right_max = height[right]
        #         else:
        #             count += right_max - height[right]
        return count
