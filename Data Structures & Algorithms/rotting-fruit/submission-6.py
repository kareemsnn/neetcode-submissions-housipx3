from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        res = 0
        while q and fresh > 0:
            for i in range(len(q)):
                (r,c) = q.popleft()

                for x, y in directions:
                    nr, nc = r + x, c + y
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            res += 1

        
        return res if fresh == 0 else -1
