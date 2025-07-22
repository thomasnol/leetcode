class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each island:
        # some sort of bfs that keeps looking until either water or edge of board
        # maybe initially start with the entire board unexplored, then run the bfs

        # While mgrid is not full of 0s, Run bfs on the first unexplored square
        # keep looking up down left right, adding coordinates to search in.
        # once searchlist is empty, add 1 to num of islands
        # only add 1 to num of islands if island had at least 1 square of space.

        # maybe initially start with the entire board unexplored, then run the bfs

        # lets get all land squares in a set
        # while there's still land to explore:
        # pick a land square, explore all around only if it's part of the set, removing from the set (ie. mark as explored land)
        # once island is explored, island_count += 1

        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        landset = set()

        for rownum in range(len(grid)):
            for colnum in range(len(grid[rownum])):
                if grid[rownum][colnum] == '1':
                    landset.add((rownum, colnum))
        
        while landset:
            to_explore = [landset.pop()]
            island_count += 1

            while to_explore:
                row, col = to_explore.pop(0)
                if col + 1 < cols and (row, col + 1) in landset:
                    to_explore.append((row, col + 1))
                    landset.remove((row, col + 1))
                if col - 1 > -1 and (row, col - 1) in landset:
                    to_explore.append((row, col - 1))
                    landset.remove((row, col - 1))
                if row + 1 < rows and (row + 1, col) in landset:
                    to_explore.append((row + 1, col))
                    landset.remove((row + 1, col))
                if row - 1 > -1 and (row - 1, col) in landset:
                    to_explore.append((row - 1, col))
                    landset.remove((row - 1, col))
        return island_count
