class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            result = max(result, curr)
        return result