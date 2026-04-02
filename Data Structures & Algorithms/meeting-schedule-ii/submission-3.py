"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = []
        endTimes = []
        result = count = 0

        for i in intervals:
            startTimes.append(i.start)
            endTimes.append(i.end)
        
        startTimes.sort()
        endTimes.sort()

        start = end = 0

        while start < len(startTimes) and end < len(endTimes):
            if startTimes[start] < endTimes[end]:
                count += 1
                start += 1
            elif startTimes[start] >= endTimes[end]:
                count -= 1
                end += 1
            result = max(result, count)

        return result

