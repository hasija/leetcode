class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        AND = [0]*32
        LEN = len(nums)
        curr = 1
        last = 0
        out = float('inf')
        def add_and(x,arr):
            for i in range(32):
                if x>>i&1:
                    pass
                else:
                    arr[i]+=1
            return arr
        
        def sub_and(x,arr):
            for i in range(32):
                if x>>i&1:
                    pass
                else:
                    arr[i]=max(arr[i]-1, 0)
            return arr
        
        
        def cal_and(arr):
            ans = 0
            for ind, i in enumerate(arr):
                ans+= 2**ind if i==0 else 0
            return ans
        
        AND = add_and(nums[0],AND)
        while curr<LEN or last<LEN:
            curr_and = cal_and(AND)
            out = min(out, abs(curr_and-k))
            if out == 0:
                return 0
            if curr_and<k:
                AND = sub_and(nums[last], AND)
                last+=1
                if last == curr and curr<LEN:
                    AND = add_and(nums[curr],AND)
                    curr+=1
            else:
                if curr<LEN:
                    AND = add_and(nums[curr],AND)
                    curr+=1
                else:
                    AND = sub_and(nums[last], AND)
                    last+=1
        return out
                    
                
            