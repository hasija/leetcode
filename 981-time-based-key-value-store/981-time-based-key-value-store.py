class TimeMap:

    def __init__(self):
        self.time_dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_dict:
            arr = self.time_dict[key]
        else:
            arr = []
        heapq.heappush(arr, (timestamp,value))
        self.time_dict[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        last_val = ""
        # print ("inside get,", key, timestamp)
        while key in self.time_dict and self.time_dict[key]:
            time, val = self.time_dict[key][0]
            if time ==timestamp:
                return val
            elif time<timestamp:
                last_val = val
                last_time = time
                heapq.heappop(self.time_dict[key])
            else:
                if last_val:
                    heapq.heappush(self.time_dict[key], (last_time, last_val))
                    return last_val
                else:
                    return ""
        if last_val:
            heapq.heappush(self.time_dict[key], (last_time, last_val))
            return last_val
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)