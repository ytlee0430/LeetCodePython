from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_x = len(grid)
        max_y = len(grid[0])

        def iterate_island(grid, x, y):
            if x + 1 < max_x and grid[x + 1][y] == "1":
                grid[x + 1][y] = "x"
                iterate_island(grid, x + 1, y)
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                grid[x - 1][y] = "x"
                iterate_island(grid, x - 1, y)
            if y + 1 < max_y and grid[x][y + 1] == "1":
                grid[x][y + 1] = "x"
                iterate_island(grid, x, y + 1)
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                grid[x][y - 1] = "x"
                iterate_island(grid, x, y - 1)

        island_count = 0
        for x in range(max_x):
            for y in range(max_y):
                if grid[x][y] == "1":
                    grid[x][y] = "x"
                    island_count += 1
                    iterate_island(grid, x, y)

        return island_count

print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))