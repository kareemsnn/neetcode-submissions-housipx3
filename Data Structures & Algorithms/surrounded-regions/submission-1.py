class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        check all the jawns connecting to the border
        for r in row
            for c in c:
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1 
                    if r,c == O:
                        dfs(r,c)

        for r in row:
            for c in col:
                if r,c == #:
                    r,c = "O"
                else:
                    r,c = "X" 
        
        def dfs():

            base case check within edges and if r,c == X:
                return

            r,c = "#"

            dfs directions
        '''

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] = "#"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        


        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == (rows - 1) or c == 0 or c == (cols-1):
                    if board[r][c] == "O":
                        dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
