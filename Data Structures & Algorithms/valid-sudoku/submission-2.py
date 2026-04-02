class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #to check row
        seen = set()
        for r in range(9):
            for i in range(9):
                if board[r][i].isalnum():
                    if board[r][i] in seen:
                        return False
                    else:
                        seen.add(board[r][i])
            seen.clear()

        #Columns
        for c in range(9):
            for i in range(9):
                if board[i][c].isalnum():
                    print(board[i][c], end = ' ')
                    if board[i][c] in seen:
                        return False
                    else:
                        seen.add(board[i][c])
            seen.clear()

        #Squares
        for square in range(9):
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col].isalnum():
                        if board[row][col] in seen:
                            return False
                        else:
                            seen.add(board[row][col])
            seen.clear()

        return True
                    
