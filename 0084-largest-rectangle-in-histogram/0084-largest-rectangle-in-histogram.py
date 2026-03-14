class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights = heights + [0]
        stack = []
        # (index and height)
        for i, h in enumerate(heights):
            prev_index = i
            while stack and stack[-1][1] > h:
                prev_index, prev_height = stack.pop() 
                           
                ans = max(ans, prev_height * (i-prev_index))
            
         
            stack.append((prev_index, h))
            
        
        return ans 