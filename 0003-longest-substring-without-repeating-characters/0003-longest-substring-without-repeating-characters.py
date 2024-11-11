class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buffer = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] in buffer:
                while s[right] in buffer:
                    buffer.remove(s[left])
                    left += 1
                buffer.add(s[right])
            else:
                buffer.add(s[right])
                max_length = max(max_length, right - left + 1)
        return max_length