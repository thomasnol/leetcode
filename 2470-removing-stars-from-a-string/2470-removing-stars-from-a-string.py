class Solution:
    def removeStars(self, s: str) -> str:
        stack = ""
        for c in s:
            if c != '*':
                stack += c
            else:
                stack = stack[:-1]
        
        return stack