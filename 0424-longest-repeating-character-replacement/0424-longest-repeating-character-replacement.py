class Solution:     
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, left to right, dynamic window size.
        # use up the k substitutions, for every possible combination
        left = 0
        freq = defaultdict(int)
        cur_len = 0
        max_freq = 0
        res = 0
        for right in range(len(s)):
            # compute expanded window
            freq[s[right]] += 1
            cur_len += 1
            max_freq = max(max_freq, freq[s[right]])
            
            # shrink window as needed
            while cur_len - max_freq > k:
                freq[s[left]] -= 1
                cur_len -= 1
                left += 1
            
            # save longest len
            res = max(res, cur_len)
        return res