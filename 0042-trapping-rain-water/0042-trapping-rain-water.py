class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
        
        # inefficient solution:
        # lmax = 0
        # rmax = 0
        # res = 0
        # # tempres = 0
        # prefix = [0] * len(height)
        # suffix = [0] * len(height)

        # prefix[0] = height[0]
        # for i in range(1, len(height)):
        #     prefix[i] = max(prefix[i-1], height[i])
        
        
        # suffix[-1] = height[-1]
        # for i in range(len(height) - 2, -1, -1):
        #     suffix[i] = max(suffix[i+1], height[i])
        
        # # print(prefix)
        # # print(suffix)
        # # return 0
        # for i in range(len(height)):
        #     res += max(0, min(prefix[i], suffix[i]) - height[i])
        # return res