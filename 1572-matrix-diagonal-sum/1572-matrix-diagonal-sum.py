class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set()
        r = len(mat)
        total = 0
        c = len(mat[0])
        for i in range(r):
            try:
                if (i,i) not in visited:
                    visited.add((i,i))
                    total += mat[i][i]
            except:
                pass
            # print (mat[i][i])
        
        for i in range(r):
            try:
                j = r-i-1
                # print (i,j)
                if (i,j) not in visited:
                    visited.add((i,j))
                    total += mat[i][j]
                    # print (mat[i][j])
            except:
                pass
            
        return total