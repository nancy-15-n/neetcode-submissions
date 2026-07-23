import bisect

class TimeMap:

    def __init__(self):
        # Dictionary: key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        # Extract timestamps for binary search
        timestamps = [t for t, _ in arr]
        
        # Find rightmost timestamp <= query
        idx = bisect.bisect_right(timestamps, timestamp) - 1
        if idx >= 0:
            return arr[idx][1]
        return ""

