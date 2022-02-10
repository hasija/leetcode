class Solution:
    def isHappy(self, n: int) -> bool:
        num_sq={}
        old_nums=set()
        old_nums.add(n)
        curr_int = str(n)
        if n==1:
            return True
        while True:
            new_val= 0
            for x in curr_int:
                if x in num_sq:
                    new_val+=num_sq[x]
                else:
                    num_sq[x]=int(x)**2
                    new_val += num_sq[x]
            if new_val in old_nums:
                return False
            elif new_val == 1:
                return True
            else:
                old_nums.add(new_val)
                curr_int = str(new_val)