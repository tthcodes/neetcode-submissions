class TimeMap:

    def __init__(self):
        # knowing that i will be storing key as keys, and then timestamp, value as pairs within a list
        # i'm gonna do defaultdict so that if a key doesn't already exist, it'll be smoothly appended to
        # an empty list 
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # here we want to set the key and timestamp + value
        self.store[key].append([timestamp, value])
        # important thing is that we know timestamp strictly increases for sets.

    def get(self, key: str, timestamp: int) -> str:
        # init ret, if no current set exists for it, just return empty str
        res = ''
        # here we can access the values for a specific key 
        values = self.store.get(key, [])
        # now we're left with a list of pairs, timestamp being first index
        # now we can initiate binary search based on timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            curTime = values[m][0]
            curVal = values[m][1]

            # compare the time to timestamp of get

            if curTime <= timestamp:
                res = curVal
                # since timestamp was less or equal to timestamp, we'll move m to the right
                # to make sure we get the most recent up to current time
                l = m + 1 
            else:
                # else if it's greater than curTime stamp, we'll move to left
                r = m - 1
        
        # after binary search done, return res
        return res

