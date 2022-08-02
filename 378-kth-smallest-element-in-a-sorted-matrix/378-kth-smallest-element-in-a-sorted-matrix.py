class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        r = c = 0
        visited = set()
        next_arr = set()
        n = len(matrix)
        while count<k:
            smallest = float('inf')
            if count==0:
                count+=1
                visited.add((r,c))
                last_r = r
                last_c = c
                if r+1<n:
                    next_arr.add((r+1,c))
                if c+1<n:
                    next_arr.add((r,c+1))
                continue
            
            for tmp_r,tmp_c in next_arr:
                if tmp_r<n and tmp_c<n and matrix[tmp_r][tmp_c] < smallest:
                    smallest = matrix[tmp_r][tmp_c]
                    new_r = tmp_r
                    new_c = tmp_c
            if new_r+1<n and (new_r+1, new_c) not in visited:
                next_arr.add((new_r+1, new_c))
            if new_c+1<n and (new_r, new_c+1) not in visited:
                next_arr.add((new_r, new_c+1))
            last_r = new_r
            last_c = new_c
            visited.add((last_r, last_c))
            next_arr.remove((new_r, new_c))
            count+=1
            # print (matrix[last_r][last_c])
        return matrix[last_r][last_c]
                    
                    