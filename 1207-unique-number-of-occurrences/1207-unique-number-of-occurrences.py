class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqmap = defaultdict(int)
        for e in arr:
            freqmap[e] += 1
        uniques = set()
        for v in freqmap.values():
            if v in uniques:
                return False
            uniques.add(v)
        return True


































        # sort arr
        # iterating left to right:
        # every time a new value is seenfreqs, add the old one to a set (seenfreqs)
        # if you're about to add a value in seenfreqs but it's already in seenfreqs, return false

        # arr.sort()
        # print(arr)
        # seenfreqs = set()
        # lastseen = 2000
        # occurences = 0
        # for e in arr:
        #     if e != lastseen:
        #         print(occurences)
        #         if occurences in seenfreqs:
        #             return False
        #         seenfreqs.add(occurences)
        #         occurences = 1
        #     else:
        #         occurences += 1
        #     lastseen = e
        # print(occurences)
        # if occurences in seenfreqs:
        #     return False
        # return True