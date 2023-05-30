class MyHashSet:

    def __init__(self):
        self.arr = [[] for i in range(1000)]


    def get_idx(self, key):
        mod = key%1000
        for idx,val in enumerate(self.arr[mod]):
            if val ==key:
                return idx
        return None
    
    def add(self, key: int) -> None:
        idx = self.get_idx(key)
        if idx is None:
            mod = key%1000
            self.arr[mod].append(key)
                

    def remove(self, key: int) -> None:
        idx = self.get_idx(key)
        if idx is not None:
            mod = key%1000
            self.arr[mod].pop(idx)

    def contains(self, key: int) -> bool:
        idx = self.get_idx(key)
        if idx is not None:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)