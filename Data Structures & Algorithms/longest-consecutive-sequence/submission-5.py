class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        arr = sorted(nums)
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if arr[i] == arr[i-1] + 1:
                current += 1
            elif arr[i] == arr[i-1]:
                continue
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)


