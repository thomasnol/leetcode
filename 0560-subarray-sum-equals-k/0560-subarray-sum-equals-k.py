class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap, mapping specific subtotal we've reached, with frequency (how many times we've reached it)
        # freqmap = defaultdict(int)
        freqmap = Counter()
        freqmap[0] = 1
        total = 0
        res = 0

        for i, n in enumerate(nums):
            total += n
            # print(total)
            if freqmap[total - k]:
                res += freqmap[total - k]
            freqmap[total] += 1
        # print(freqmap)
        return res
            