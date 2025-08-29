class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # map (bool, int) -> int
        mapping = {}
        def f(own, day):
            if day >= len(prices):
                return 0
            if (own, day) in mapping:
                return mapping[(own, day)]
            if own:
                act = f(False, day + 1) + prices[day]
            else:
                act = f(True, day + 1) - prices[day]
               
            not_act = f(own, day + 1)
            max_profit = max(act, not_act)
            mapping[(own, day)] = max_profit
            return max_profit
        return f(False, 0)
        
    