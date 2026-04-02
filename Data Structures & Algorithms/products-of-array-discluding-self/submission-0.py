class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        result = 0

        for i in range(len(nums)):
            result = math.prod(nums[:i] + nums[i + 1:])
            output.append(result)
        return output