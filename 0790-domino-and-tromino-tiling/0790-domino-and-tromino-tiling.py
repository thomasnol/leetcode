class Solution:
    def numTilings(self, n: int) -> int:
        # 1
        # 2
        # 5
        # 11
        # 24
        # 53
        # 117
        # 53 * 2 = 106
        # 117 - 106 = 11
        # 24 * 2 = 48
        # 53 - 48 = 5
        # we could find a general formula to calculate res for 2 x n.
        # or maybe there's a way to use dynamic programming to calculate the answer
        # base cases would be 2 x 1 and 2 x 2
        # seems like the answer of 2 x n is likely 2(2 x n/2) + some amount, likely constant
        # the extra amount X should be when there's a domino in the slice: could be 1 domino, 2 dominos or 1 tromino:
        # if 1 domino, handle as board 2 x n-1 (unsure)
        # if 2 dominos, handle as board 2 x n-2, * 2 bc 2 options
        # if 1 tromino, no idea how to handle, * 4 bc 4 options

        # we have full and partial states (full is where the board is rectangular, partial means both row lengths vary by 1)
        # we say full(10) is a board of 2x10 and partial(10) is a board of 2x9 with an extra square
        # full(n) = full(n-1) + full(n-2) + 2(partial(n-1))
        # partial(n) = full(n-2) + partial(n-1)
        # full(0) = 0, full(1) = 1, full(2) = 2
        # partial(0) = 0, partial(1) = 0, partial(2) = 1
        # @lru_cache for now, recursive
        @lru_cache
        def full(n):
            if n <= 0: return 0
            if n == 1: return 1
            if n == 2: return 2
            # print(full(n-1))
            # print(full(n-2))
            # print(partial(n-1))
            return full(n-1) % (10**9+7) + full(n-2) % (10**9+7) + 2 * (partial(n-1)) % (10**9+7)
        @lru_cache
        def partial(n):
            if n <= 0: return 0
            if n == 1: return 0
            if n == 2: return 1
            return full(n-2) % (10**9+7) + partial(n-1) % (10**9+7)
        return full(n) % (10**9+7)
        # alternatively we can just do bottom-up, knowing x_n = 2(x_n-1) + x_n-3: so 11 = 2(5) + 1