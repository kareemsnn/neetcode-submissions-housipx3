class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        '''
        dfs(currentVal):

            if currentVal == amount:
                return 0

            if currentVal in memo:
                return memo[currentVal]

            result = 0
            for num in nums:
                result = min(result, 1 + dfs(currentVal - 1))
            
            memo[currentVal] = result

            return result
        '''

        def dfs(curr):
            if curr == 0:
                return 0

            if curr in memo:
                return memo[curr]
            
            res = 10000
            for num in coins:
                if curr - num >= 0:
                    res = min(res, 1 + dfs(curr - num))

            memo[curr] = res
            return res

        out = dfs(amount)
        return out if out != 10000 else -1