class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                current = 0
                while (num + current) in numSet:
                    current += 1
                longest = max(longest, current)

        return longest


