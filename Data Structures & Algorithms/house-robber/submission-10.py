class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        store dp[0] and dp[1]
        dp[i] = dp[i - 1] or dp[i - 2] + curr
        '''

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
        print(dp)
        return dp[-1]