class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        see if each cell can be reached from each ocean
        for all cells on the top border, dfs downwards
        for all cells on bottom border, dfs upwards.
        for all cells on the right and left, dfs inwards
        if seen add to visited to optimize
        '''

        rows, cols = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(row, col, visited, prev):
            if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited:
                return
            
            if heights[row][col] < prev:
                return

            visited.add((row,col))

            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])


        for row in range(rows):
            dfs(row, 0, pac, -1)
            dfs(row, cols-1, atl, -1)
        
        for col in range(cols):
            dfs(0, col, pac, -1)
            dfs(rows-1, col, atl, -1)

        result = []
        for cell in (pac & atl):
            result.append(cell)
        
        return result