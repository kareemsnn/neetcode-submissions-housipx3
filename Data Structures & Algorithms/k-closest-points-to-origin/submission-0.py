class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        given 2d array. point[i] = [xi, yi] coords. 
        return k nearest points to 0,0

        to determine distance, calculate euclidean distance

        -----------------

        res = []

        for point in points:
            distance = 

        '''

        heap = []

        for point in points:
            x,y = point[0], point[1]
            distance = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap,(distance, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res