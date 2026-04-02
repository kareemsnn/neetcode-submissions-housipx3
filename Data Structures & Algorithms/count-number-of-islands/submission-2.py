class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        with a nested for loop, go thru the matrix till you find 1
        once found, dfs(row, col)

        within dfs, check boundaries, then turn that coord to 0
        dfs all directions
        res += 1
        '''

        
        rows,cols = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row,col)
                    res += 1

        return res


        