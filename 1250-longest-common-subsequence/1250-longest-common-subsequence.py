class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mapping = {}
        def f(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0
            if (p1, p2) in mapping:
                return mapping[(p1, p2)]
            if text1[p1] == text2[p2]:
                mapping[(p1, p2)] = f(p1 + 1, p2 + 1) + 1
                return mapping[(p1, p2)]
            mapping[(p1, p2)] = max(f(p1 + 1, p2), f(p1, p2 + 1))
            return mapping[(p1, p2)]
        return f(0, 0)