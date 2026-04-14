from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        for loop and append treasure to queue

        while q:
            value, i, j = q.pop
            if value > grid[r][c]:
                continue

            grid[r][c] = value
            for directions:
                if r and c within bounds and grid[r][c] != -1:
                    q.append(value + 1, nr, nc)
        '''

        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((0,r,c))
        
        while q:
            value, r, c = q.popleft()

            if value > grid[r][c]:
                continue
            
            grid[r][c] = value
            for x, y in directions:
                nr, nc = r + x, c + y
                if nr < rows and nr >= 0 and nc >= 0 and nc < cols and grid[nr][nc] != -1:
                    q.append((value + 1, nr, nc))
            
        # return grid







        