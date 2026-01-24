class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # lets just map rows to an int
        # then compare every row to the dictionary and increment the count accordingly
        # we can't just use a set bc then several rows being identical won't count double as it should
        # res = 0
        # row_count = {}
        # n = len(grid)
        # for r in grid:
        #     row_count[tuple(r)] = row_count.get(tuple(r), 0) + 1
        # for i in range(n):
        #     col = tuple([grid[j][i] for j in range(n)])
        #     res += row_count.get(col, 0)
        # return res


        # this also works:
        from collections import Counter

        n = len(grid)
        rows = Counter(tuple(r) for r in grid)              # Count row patterns
        cols = Counter(tuple(grid[j][i] for j in range(n)) for i in range(n))  # Count column patterns
        return sum(rows[k] * cols[k] for k in rows)         # Multiply matches
