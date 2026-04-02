class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # result = []

        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # while k:
        #     maxVal = 0
        #     maxKey = 0
        #     for key, value in freq.items():
        #         if value > maxVal:
        #             maxVal = value
        #             maxKey = key
        #     result.append(maxKey)
        #     freq.pop(maxKey)
        #     k -= 1
            
        # return result

        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for count, num in heap]
        return result


