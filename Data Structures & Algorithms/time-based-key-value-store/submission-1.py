from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        
        timestamps = self.keyStore[key]
        ind = timestamps.bisect_right(timestamp) - 1

        if ind >= 0:
            closest = timestamps.iloc[ind]
            return timestamps[closest]
        
        return ""