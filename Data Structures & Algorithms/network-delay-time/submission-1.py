from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        intuition:
        start from node K
        have an adj list containing each with it's neighbors.
        for each node, append neighbors to min heap.
        pop next node from min heap

        visited list to keep track of what was processed

        once len(visited) = n, return current weight
        '''
        
        adjList = defaultdict(list)
        seen = set()

        for start, end, weight in times:
            adjList[start].append((weight, end))
        
        heap = [(0, k)]
        res = 0

        while heap:
            weight, start = heapq.heappop(heap)
            if start in seen:
                continue
            
            res = weight
            seen.add(start)

            for w, node in adjList[start]:
                if node not in seen:
                    heapq.heappush(heap, (w + weight, node))

        print(seen)
        return res if len(seen) == n else -1
