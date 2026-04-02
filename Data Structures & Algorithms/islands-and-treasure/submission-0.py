class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row,col))

        def addBox(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r,c) in visited:
                return
            visited.add((r,c))
            queue.append([r,c])


        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                addBox(row + 1, col)
                addBox(row - 1, col)
                addBox(row, col + 1)
                addBox(row, col - 1)
                grid[row][col] = distance
            distance += 1