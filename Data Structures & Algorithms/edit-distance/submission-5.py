class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Brute Force psuedocode

        if len(word1)
        dfs(i, j):


        '''

        #BRUTE FORCE
        '''
        if len(word1) == 0 and len(word2) == 0:
            return 0

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            res = min(dfs(i, j + 1), dfs(i + 1, j))
            res = min(res, dfs(i + 1, j + 1))

            return res + 1
        
        return dfs(0,0)
        '''

        #MEMOIZATION
        # if len(word1) == 0 and len(word2) == 0:
        #     return 0
        # memo = {}

        # def dfs(i, j):
        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i
            
        #     if (i, j) in memo:
        #         return memo[(i,j)]

        #     if word1[i] == word2[j]:
        #         memo[(i, j)] = dfs(i + 1, j + 1)
        #     else:
        #         res = min(dfs(i, j + 1), dfs(i + 1, j))
        #         res = min(res, dfs(i + 1, j + 1))
        #         memo[(i,j)] = res + 1
        #     return memo[(i,j)]
        
        # return dfs(0,0)

    #2D BOTTOM UP
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for j in range(len(word1) + 1):
            dp[len(word2)][j] = len(word1) - j
        for i in range(len(word2) + 1):
            dp[i][len(word1)] = len(word2) - i

        for i in range(len(word2) - 1, -1, -1):
            print(i)
            for j in range(len(word1) - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    res = min(dp[i + 1][j], dp[i][j + 1])
                    res = min(res, dp[i + 1][j + 1])
                    dp[i][j] = res + 1

        return dp[0][0]