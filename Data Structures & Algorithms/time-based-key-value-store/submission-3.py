class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, entries = "", self.vals.get(key,[])
        l, r = 0, len(entries)-1
        while l <= r:
            m = l + (r-l)//2
            if entries[m][1] <= timestamp:
                res = entries[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
