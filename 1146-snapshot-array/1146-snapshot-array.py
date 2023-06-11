class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{"latest":0, "prev":0} for i in range(length)]
        self.len = length
        self.snap_id = 0
        self.change = set()
    def set(self, index: int, val: int) -> None:
        self.arr[index]['latest']=val
        if self.arr[index]['latest']!=self.arr[index]['prev']:
            self.change.add(index)
        else:
            try:
                self.change.remove(index)
            except:
                pass
    def snap(self) -> int:
        for i in self.change:
            val = self.arr[i]
            val[self.snap_id]=val['latest']
            val['prev'] = val['latest']
        
        self.snap_id+=1
        self.change = set()
        # print (self.arr) 
        return self.snap_id-1
                    
    def get(self, index: int, snap_id: int) -> int:
        val = self.arr[index]
        res = 0
        latest = val['latest']
        prev = val['prev']
        val.pop('latest')
        val.pop('prev')
        # bisect left
        keys = list(val.keys())
        # keys_set = set(keys)
        idx = bisect.bisect_left(keys,snap_id)
        # print ("get, bisect index", idx)
        # print (idx, keys)
        try:
            if idx < len(keys) and keys[idx] == snap_id:
                # print ("snap id matched")
                res= val[snap_id]
            else:
                new_snap = idx-1
                # print ("new snap id", new_snap)
                if new_snap>=0:
                    
                    key = keys[new_snap]
                    res =  val[key]
                    # print ("res", res)
                else:
                    res = 0
                    # print ("less than 1", res)
        except Exception as e:
            # print ("something failed", str(e))
            res = 0
        val['latest'] = latest
        val['prev'] = prev
        return res
            


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)