class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        loop through the board till we find the first character of word
        then dfs(index, currentString)
        for all the nodes around C, dfs

        0 : dfs(0,row, col, [C])

        result = ["C", ]

        rows, cols = 

        dfs(wordIndex, row, col, current):

            if row < 0 and col < 0 and row >=rows and col >= cols and matrix[row][col] != word[wordIndex]:
                return

            result.append(current[:])
            
            current.append(char)

            dfs(wordIndex + 1, row + 1, col, current)
            dfs(wordIndex + 1, row - 1, col, current)
            dfs(wordIndex + 1, row, col + 1, current)
            dfs(wordIndex + 1, row, col - 1, current)

            current.pop()
        '''



        result = []
        visited = set()

        rows, cols = len(board), len(board[0])

        def dfs(wordIndex, row, col):

            if wordIndex == len(word):
                return True

            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[wordIndex] or (row,col) in visited:
                return False

            visited.add((row, col))

            res = (dfs(wordIndex + 1, row + 1, col) or
            dfs(wordIndex + 1, row - 1, col) or
            dfs(wordIndex + 1, row, col + 1) or 
            dfs(wordIndex + 1, row, col - 1))

            visited.discard((row,col))
            return res


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(0, row, col):
                        return True
        return False

            
