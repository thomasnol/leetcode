class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # goal is dp (maps amount to # of coins)
        # start at 0, fill in the mapping with every possible coin
        dp = {}
        # dp = defaultdict(int)
        dp[0] = 0
        for i in range(amount + 1):
            if i in dp:
                for c in coins:
                    if (i + c) in dp:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
                    else:
                        dp[i + c] = dp[i] + 1
            else:
                dp[i] = float('inf')
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]