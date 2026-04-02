class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        '''
        start at amount

        for each coin, dfs then memoize whatever it finds
        take the min between current res and dfs result

        '''

        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            
            if amount ==0:
                return 0

            minCoin = float("inf")
            for coin in coins:
                if amount - coin >=0:
                    minCoin = min(minCoin, 1 + dfs(amount - coin))
            
            memo[amount] = minCoin
            return minCoin

        

        result = dfs(amount)
        return -1 if result >= 100000 else result