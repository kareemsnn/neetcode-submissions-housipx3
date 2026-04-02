class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            if x >= row or x < 0 or y >= col or y < 0 or grid[x][y] == 0 or (x,y) in visited:
                return 0
                
            visited.add((x,y))
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)


        for i in range(row):
            for j in range(col):
                result = max(result, dfs(i, j))
        
        return result
