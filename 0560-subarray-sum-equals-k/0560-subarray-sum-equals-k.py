class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap, mapping specific subtotal we've reached, with frequency (how many times we've reached it)
        freqmap = defaultdict(int)
        freqmap[0] = 1
        total = 0
        res = 0

        for i, n in enumerate(nums):
            total += n
            # print(total)
            if freqmap[total - k]:
                res += freqmap[total - k]
                # if freqmap[total - k] == 0:
                #     print("BAD")
            freqmap[total] += 1
        return res
            