class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        new_mat = [[0]*rows for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                new_mat[j][i]=mat[i][j]
        return new_mat