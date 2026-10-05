class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if not self.hashmap[key]:
            return ""
        minimum_timestamp = self.hashmap[key][0][0]
        if timestamp < minimum_timestamp:
            return ""

        l, r = 0, len(self.hashmap[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.hashmap[key][mid][0] == timestamp:
                return self.hashmap[key][mid][1]
            elif self.hashmap[key][mid][0] < timestamp:
                ans = self.hashmap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
