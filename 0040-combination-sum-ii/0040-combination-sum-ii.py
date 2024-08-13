class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        def dfs(used, left):
            # print ("used",used, left)
            if sum(used)==target:
                if tuple(used) not in self.ans:
                    self.ans.add(tuple(used))
            elif sum(used)>target:
                return
            
            curr = sum(used)
            for idx, i in enumerate(left):
                if curr+i>target:
                    break
                if idx>0 and i == left[idx-1]:
                    continue
                dfs(used+[i], left[idx+1:])
        
        dfs([],sorted(arr))
        return self.ans
                