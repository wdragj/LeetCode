class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        else:
            timestamps = self.times[key]
            l, r = 0, len(timestamps) - 1
            val = ""

            while l <= r:
                mid = (l + r) // 2
                
                # Mid pointer less than timestamp
                if timestamps[mid][0] <= timestamp:
                    val = timestamps[mid][1]
                    l = mid + 1
                # Mid pointer greater than timestamp
                else:
                    r = mid - 1
            return val
                  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)