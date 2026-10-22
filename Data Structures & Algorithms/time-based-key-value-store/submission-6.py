class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            m = (l + r) // 2
            mTime = self.store[key][m][1]
            if mTime <= timestamp:
                res = self.store[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return res