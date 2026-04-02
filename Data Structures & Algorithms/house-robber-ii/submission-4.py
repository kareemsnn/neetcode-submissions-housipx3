class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])

        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        for j in range(3, n):
            dp2[j] = max(dp2[j - 1], dp2[j - 2] + nums[j])

        print(dp1)
        print(dp2)
        return max(dp1[-2], dp2[-1])