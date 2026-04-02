class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [False] * len(nums)

        # dp[-1] = True

        # for i in range(len(nums) - 2, -1, -1):
        #     end = min(len(nums), i + nums[i] + 1)
        #     for j in range(i, end):
        #         print(j)
        #         if dp[j] == True:
        #             dp[i] = True
        #             break

        # return dp[0]

        end = len(nums) - 1
        for i in range(end - 1, -1, -1):
            if (nums[i] + i) >= end:
                end = i
        
        return end == 0