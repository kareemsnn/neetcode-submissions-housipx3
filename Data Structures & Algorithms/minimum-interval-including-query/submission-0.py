class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        lengths = {}

        for i, j in intervals:
            lengths[(i,j)] = (j - i + 1)

        res = []
        for query in queries:
            curr = float('inf')
            for k, l in lengths.items():
                if query <= k[1] and query >= k[0]:
                    curr = min(curr, l)

            res.append(curr) if curr != float("inf") else res.append(-1)
        
        return res