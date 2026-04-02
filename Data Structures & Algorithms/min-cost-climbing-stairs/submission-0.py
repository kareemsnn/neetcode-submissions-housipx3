class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        we have the smaller sub problem which is, at each index, what's the lowest we can take

        [1,2,?]
        for each index
            choose either min([index - 2] + val, index-1 + val)
            if index + 1 or + 2 ? len(cost):
                return answ
        '''
        if len(cost) <= 2:
            return min(cost)

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            print(cost[i])
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])
                
        return min(dp[-1],dp[-2])
