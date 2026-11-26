# Time Based Key-Value Store (LeetCode 981) - Binary Search
# Approach: store[key] = list of [value, timestamp]. set() only appends, and
#           timestamps arrive in increasing order, so each list is already
#           sorted by timestamp. get() binary searches that list for the
#           largest timestamp <= the given one: when values[mid][1] <= timestamp,
#           it's a candidate (save it, look right for a later one); otherwise
#           look left. Return "" if nothing qualifies.
#           Bug fixed on the way: set() needs `if key not in self.store`
#           (with `in`, a new key raised KeyError).
# Time: set O(1), get O(log n)  |  Space: O(total number of set calls)

class TimeMap:

    def __init__(self):
        self.store = {} #Key : Str and Val: [value,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        # Get a list of all the values
        values = self.store.get(key,[])
        
        left, right = 0, len(values) - 1
        # Binary search
        while left <= right:
            mid = (left+right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0] #Return the value not the timestamp
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
