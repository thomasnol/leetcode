class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts = [0] + cuts + [n]
        
        cuts.sort()
        
        m = len(cuts)
        
        dp = [[0] * (m+2) for _ in range(m+2)]
        # dp as [left][right] # aka same cuts to do so same result
        # dp as [stick_len][cut_index]
        # min(n - 1, 100)
        # cost = 1e9
        for left in range(m-1, -1, -1):
            for right in range(left+1, m):
                    
       
                for cut_index in range(left+1, right):
                    cut_val = cuts[cut_index]
                    # dp[left][cut_index-1]
                    left_substick = dp[left][cut_index]
                    right_substick = dp[cut_index][right]
                    # cost = min(cost, left_substick + right_substick + cuts[right] - cuts[left])
                    dp[left][right] = min(1e9 if dp[left][right] == 0 else dp[left][right], left_substick + right_substick + cuts[right] - cuts[left])
                # dp[left][right] = cost
        
        return dp[0][len(cuts) - 1] 


# class Solution:
#     def minCost(self, n: int, cuts: List[int]) -> int:
#         cuts.sort()
        
#         @cache
#         def f(start_stick, end_stick, left, right):
           
#             if left > right:
#                 return 0
            
#             cost = 1e9
            
#             for cut_index in range(left, right+1):
#                 cut_val = cuts[cut_index]
#                 left_substick = f(start_stick, cut_val, left, cut_index-1)
#                 right_substick = f(cut_val, end_stick, cut_index+1, right)
#                 cost = min(cost, left_substick + right_substick + end_stick - start_stick)
            
#             return cost
        
#         return f(0, n, 0, len(cuts)-1)
        