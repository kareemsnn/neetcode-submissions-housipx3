class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [(0, 30)]
        pop, result[0] = i - 0
        [(1,38)]
        [(1,38), (2, 30)]
        pop, result[2] = i - 2
        [(1,38), (3, 36)]
        [(1,38), (3, 36), (4, 35)]
        pop, results[4] = i - 4
        pop, results[3] = i - 3
        '''

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()
                result[index] = i - index
            stack.append((i, temperatures[i]))
        
        return result