import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        

        while len(maxHeap) >= 2:
            print(maxHeap)
            #top two stones:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                stone1 = stone1 - stone2
                heapq.heappush(maxHeap, -stone1)
            elif stone2 > stone2:
                stone2 = stone2 - stone2
                heapq.heappush(maxHeap, -stone2)
            
        return -maxHeap[0] if maxHeap else 0