class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Condition to find local minimum: l >= m <= r
        mapping = defaultdict(int) # maps idx to candies received, for peaks
        candies = 0
        numratings = len(ratings)
        for ogroot in range(numratings):
            if ogroot - 1 >= 0 and ratings[ogroot - 1] < ratings[ogroot]:
                continue
            if ogroot + 1 < numratings and ratings[ogroot + 1] < ratings[ogroot]:
                continue
            # print(ogroot)

            root = ogroot
            candies += 1
            curcandy = 1
            candytoadd = 0
            while root - 1 >= 0 and ratings[root - 1] > ratings[root]:
                curcandy += 1
                candytoadd = max(curcandy - mapping[root - 1], 0)
                candies += candytoadd
                root -= 1
            mapping[root] = candytoadd
            root = ogroot
            curcandy = 1
            while root + 1 < numratings and ratings[root + 1] > ratings[root]:
                curcandy += 1
                candytoadd = max(curcandy - mapping[root + 1], 0)
                candies += candytoadd
                root += 1
            mapping[root] = candytoadd
        return candies