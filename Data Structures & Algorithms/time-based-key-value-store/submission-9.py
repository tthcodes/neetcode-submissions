class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        stores key with value at given time 

        ALL timestamps of set are STRICTLY INCREASING - tells me that there's an efficient way to 
        sort through using binary search here 

        for the value of each key, we can set it to a list, in which we append PAIRS, [timestamp, value]

        then we perform binary search on the first index to find the val and return for get
        '''

        self.timeMap[key].append((timestamp, value))


        

    def get(self, key: str, timestamp: int) -> str:
        '''
        retrieves the value at a given key/time pair. the output is a str

        here when we retrieve we can use binary search to find the proper return 

        returns a value in which set was called before AND previous timestamp is <= CURRENTLY INPUT timestamp... if NO values, it returns ""
        '''

        l, r = 0, len(self.timeMap[key]) - 1

        val = ""

        if not self.timeMap[key]:
            return val

        # return the LATEST set time if there are MULTIPLE timestamps <= input time
        while l <= r:
            m = (l + r) // 2
            curTime = self.timeMap[key][m][0]
            if curTime > timestamp:
                r = m - 1
                continue
            else:
                val = self.timeMap[key][m][1]
                l = m + 1
        
        return val
