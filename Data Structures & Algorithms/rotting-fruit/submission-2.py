from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        fresh = 0
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                
                for x, y in directions:
                    nr, nc = r + x, c + y

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            res += 1

        
        if fresh == 0:
            return res
        else:
            return -1
