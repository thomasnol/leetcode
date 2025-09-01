class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # cuts = [0] + cuts + [n]
        
        cuts.sort()
        # left, right side of stick -> important 
        # length of stick
        # list of cuts for the stick, absolute or relative
        # output is total cost
        
        # start stick, end stick (left, right side)
        # left and right as indexes of relevent cuts to do
        [1,3,4,6]
        [0,1,2,3,4,5,6,7]
        
        [4,5,6]
        [4,5,6,7]
        
        @cache
        def f(start_stick, end_stick, left, right):
           
            if left > right:
                return 0
            
            cost = 1e9
            
            for cut_index in range(left, right+1):
                
                cut_val = cuts[cut_index]
                left_substick = f(start_stick, cut_val, left, cut_index-1)
                right_substick = f(cut_val, end_stick, cut_index+1, right)
                cost = min(cost, left_substick + right_substick + end_stick - start_stick)
            
            return cost
        
        return f(0, n, 0, len(cuts)-1)
        

        