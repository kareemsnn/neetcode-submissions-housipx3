class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        dfs(r, c, prev):
            if outta bounds or prev >= matrix[r][c]:
                return -1
            
            res = -1
            res = max(res, 1 + dfs(r ,c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c))
            return res
        '''

        #BRUTE FORCE
        '''
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or prev >= matrix[r][c]:
                return -1
            
            res = -1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            return res

        result = -1
        for r in range(rows):
            for c in range(cols):
                result = max(result, 1 + dfs(r, c, -1))
        return result
        '''

        #TOP DOWN MEMOIZATION
        # rows, cols = len(matrix), len(matrix[0])
        # memo = {}
        # directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        # def dfs(r, c):
        #     if (r,c) in memo:
        #         return memo[(r,c)]

        #     # if r < 0 or c < 0 or r >= rows or c >= cols or prev >= matrix[r][c]:
        #     #     memo[(r,c)] = -1
        #     #     return -1
            
        #     res = -1
        #     for x, y in directions:
        #         if r+x < 0 or c+y < 0 or r+x >= rows or c+y >= cols or matrix[r][c] >= matrix[r+x][c+y]:
        #             continue
        #         res = max(res, 1 + dfs(r + x, c + y))

        #     # res = max(res, 1 + dfs(r + 1, c))
        #     # res = max(res, 1 + dfs(r - 1, c))
        #     # res = max(res, 1 + dfs(r, c + 1))
        #     # res = max(res, 1 + dfs(r, c - 1))
        #     memo[(r,c)] = res
        #     return res


        # result = -1
        # for r in range(rows):
        #     for c in range(cols):
        #         result = max(result, 1 + dfs(r, c))
        # return result + 1

        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or prev >= matrix[r][c]:
                return -1
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = -1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            memo[(r, c)] = res
            return res

        result = -1
        for r in range(rows):
            for c in range(cols):
                result = max(result, 1 + dfs(r, c, -1))

        return result