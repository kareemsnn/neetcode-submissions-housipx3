class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = float('-inf')

        def dfs(r,c):
            '''
            #BASE CASE: CHECK BOUNDS AND R,C == 0: RETURN

            turn current grid == 0
            res = (1 + dfs(directions))
            return res
            '''

            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            res = (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r,c + 1) + dfs(r, c - 1))
            return res


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result = max(result, dfs(row,col))
            
        return 0 if result == float('-inf') else result 