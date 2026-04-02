class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        #BRUTE FORCE:
        new output arr
        iterate thru the list, if we find a start time greater than newInterval's start:
            append it there
            then append intervals[i]
        else:
            append intervals[i]
        '''

        output = []
        inserted = False

        for i in range(len(intervals)):
            if not inserted and newInterval[0] < intervals[i][0]:
                output.append(newInterval)
                inserted = True
            output.append(intervals[i])
        
        if not inserted:
            output.append(newInterval)

        if len(output) <= 1:
            return output

        res = [output[0]]
        for i in range(1, len(output)):
            if res[-1][1] >= output[i][0]:
                res[-1][1] = max(res[-1][1], output[i][1])
            else:
                res.append(output[i])

        return res