class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap, mapping specific subtotal we've reached, with frequency (how many times we've reached it)
        freqmap = defaultdict(int)
        # freqmap = Counter()
        freqmap[0] = 1
        total = 0
        res = 0

        for n in nums:
            total += n
            # print(total)
            if total - k in freqmap:
                res += freqmap[total - k]
            freqmap[total] += 1
        # print(freqmap)
        return res
            