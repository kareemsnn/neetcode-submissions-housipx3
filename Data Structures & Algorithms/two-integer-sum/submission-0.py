class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = 0
        seen = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference not in seen:
                seen[num] = index
            else:
                return [seen[difference], index]
