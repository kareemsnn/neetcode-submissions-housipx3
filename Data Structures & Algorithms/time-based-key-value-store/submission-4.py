from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)      

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        #ASSUME ALWAYS SORTED
        '''BRUTE FORCE'''
        # seen = 0
        # val = ""
        # for time, v in self.store[key]:
        #     if time <= timestamp:
        #         seen = time
        #         val = v
        
        # return val

        '''
        alice happy 1
        alice sad 5
        alice x 10
        alice nig 15
        alice   y 20
        get alice at 17

        so if less than timestamp, store it for now
        if greater, decrement r
        '''

        l, r = 0, len(self.store[key])
        vals = self.store[key]
        res = ""

        while l < r:
            m = (l + r) // 2

            # if vals[m][0] == timestamp:
            #     return vals[m][1]
            
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l += 1

            if vals[m][0] > timestamp:
                r -= 1

        return res