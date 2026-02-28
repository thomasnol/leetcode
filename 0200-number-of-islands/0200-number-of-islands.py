class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs from every land square? and we simply count how many dfs rounds we started
        # we'll just modify the initial grid, turning land into water as we iterate
        ret = 0
        stack = []
        ranges = [[-1,0], [0,-1], [1,0], [0,1]]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    ret += 1
                    stack.append((row, col))
                    while stack:
                        r, c = stack.pop()
                        # print((r, c))
                        for modifier in ranges:
                            nr = r + modifier[0]
                            nc = c + modifier[1]
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                                if grid[nr][nc] == "1":
                                    grid[nr][nc] = "0"
                                    stack.append((nr, nc))
        return ret
