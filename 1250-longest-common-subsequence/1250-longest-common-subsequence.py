class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # could start at end and reconstitute the mapping?
        # start with the strings from left to right??
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]





































        # mapping = {}
        # def f(p1, p2):
        #     if p1 >= len(text1) or p2 >= len(text2):
        #         return 0
        #     if (p1, p2) in mapping:
        #         return mapping[(p1, p2)]
        #     if text1[p1] == text2[p2]:
        #         mapping[(p1, p2)] = f(p1 + 1, p2 + 1) + 1
        #         return mapping[(p1, p2)]
        #     mapping[(p1, p2)] = max(f(p1 + 1, p2), f(p1, p2 + 1))
        #     return mapping[(p1, p2)]
        # return f(0, 0)