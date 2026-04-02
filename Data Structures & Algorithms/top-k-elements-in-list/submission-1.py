class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []

        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1

        while k:
            maxVal = 0
            maxKey = 0
            for key, value in freq.items():
                if value > maxVal:
                    maxVal = value
                    maxKey = key
            result.append(maxKey)
            freq.pop(maxKey)
            k -= 1
            
        return result