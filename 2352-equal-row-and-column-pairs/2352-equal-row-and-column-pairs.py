class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_dict = collections.defaultdict(int)
        n = len(grid)
        new_arr = [[0]*n for i in range(n)]
        
        for idx, row in enumerate(grid):
            val = tuple(row)
            count_dict[val]+=1
            for i in range(n):
                new_arr[i][idx] = val[i]
        count = 0
        # print (count_dict)
        # print ("new arr", new_arr)
        for col in new_arr:
            val = tuple(col)
            count+=count_dict[val]
        return count
        