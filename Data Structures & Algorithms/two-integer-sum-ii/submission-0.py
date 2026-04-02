class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(numbers):
            diff = target - num
            if diff not in hashmap:
                hashmap[num] = index + 1  # storing 1-indexed position
            else:
                return [hashmap[diff], index + 1]