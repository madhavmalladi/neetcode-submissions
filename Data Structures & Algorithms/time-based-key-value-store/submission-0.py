from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # run binary search to find the closest timestamp (or equal)
        if key not in self.hashmap:
            return ""
        
        ans = ""
        l, r = 0, len(self.hashmap[key]) - 1
        arr = self.hashmap[key]

        while l <= r:
            mid = (l + r) // 2
            if (arr[mid][0] == timestamp):
                return arr[mid][1]
            elif (arr[mid][0] <= timestamp):
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
        
