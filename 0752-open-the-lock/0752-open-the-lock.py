class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadends = list(map(list,deadends))
        for item in deadends:
            visited.add(tuple(map(int, item)))
        # print (visited)
        start = tuple([0,0,0,0])
        target = tuple(map(int,list(target)))
        ans = 0
        arr = [start]
        while arr:
            new_arr = []
            for curr in arr:
                if curr in visited:
                    continue
                if curr == target:
                    return ans
                visited.add(tuple(curr))
                
                for ind, val in enumerate(curr):
                    new_val1 = 0 if val == 9 else val+1
                    new_val2 = 9 if val == 0 else val-1
                    tmp1 = tuple(list(curr[:ind])+[new_val1]+list(curr[ind+1:]))
                    tmp2 = tuple(list(curr[:ind])+[new_val2]+list(curr[ind+1:]))
                    if tmp1 not in visited:
                        new_arr.append(tmp1)
                    if tmp2 not in visited:
                        new_arr.append(tmp2)

            arr = new_arr
            # print ("new one",arr)
            ans+=1
        return -1