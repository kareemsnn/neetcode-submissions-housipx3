from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        bfs.

        Start at root node = 1
        deque has [node, weight]
        deque = ([k, 0])

        while q:
            
        '''
        adjList = defaultdict(list)
        for start, end, weight in times:
            adjList[start].append((end, weight))
        
        heap = [(0, k)]
        seen = set()
        res = 0

        while heap:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue

            seen.add(node)
            res = weight

            for nei, w in adjList[node]:
                if nei not in seen:
                    heapq.heappush(heap, (w + res, nei))
        
        return res if len(seen) == n else -1