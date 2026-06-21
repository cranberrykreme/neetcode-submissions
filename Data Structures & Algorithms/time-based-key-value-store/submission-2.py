class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals.setdefault(key, {})[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        entries = self.vals[key]
        while timestamp > 0 and timestamp not in entries:
            timestamp -= 1
        return entries[timestamp] if timestamp in entries else ""
