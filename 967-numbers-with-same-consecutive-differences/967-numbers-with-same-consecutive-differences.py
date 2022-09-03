class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.out = set()
        def recurse(curr_num, count):
            if count==0:
                self.out.add(int(curr_num))
                return
            last_val = int(curr_num[-1])
            if last_val+k>=10 and last_val-k<0:
                return
            if last_val+k<10:
                recurse(curr_num+str(last_val+k), count-1)
            if last_val-k>=0:
                recurse(curr_num+str(last_val-k), count-1)
                
        for i in range(1, 10):
            recurse(str(i),n-1)
        return self.out
            
            
            