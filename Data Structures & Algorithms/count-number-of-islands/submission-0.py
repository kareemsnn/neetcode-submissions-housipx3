class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(x, y):
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0 or grid[x][y] == "0":
                return
            grid[x][y] = "0"

            dfs(x + 1,  y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)


        for rows in range(len(grid)):
            for cols in range(len(grid[0])):
                if grid[rows][cols] == "1":
                    dfs(rows, cols)
                    count += 1

        return count

