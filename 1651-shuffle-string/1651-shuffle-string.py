class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        for i in range(len(s)):
            # res[i] = s[indices[i]]
            res[indices[i]] = s[i]
        res = "".join(res)
        return res