class MyHashSet:
    
    def eval_bucket(self, key):
        hashed = key%self.mod_val
        return hashed
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod_val = 500
        self.arr=[[] for x in range(self.mod_val)]
        
    def add(self, key: int) -> None:
        if self.contains(key):
            pass
        else:
            hash_val = self.eval_bucket(key)
            self.arr[hash_val].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            hash_val = self.eval_bucket(key)
            self.arr[hash_val].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_val = self.eval_bucket(key)
        if key in self.arr[hash_val]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)