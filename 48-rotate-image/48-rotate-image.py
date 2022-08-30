class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for row in range(len(matrix)//2):
            for col in range(row, len(matrix[0])-1-row):
                tmp1 = matrix[col][n-row]
                tmp2 = matrix[n-row][n-col]
                tmp3 = matrix[n-col][row]
                matrix[col][n-row] = matrix[row][col]
                matrix[n-row][n-col] = tmp1
                matrix[n-col][row] = tmp2
                matrix[row][col]= tmp3
                # tmp = matrix[row][n-col]
                # matrix[row][n-col] = matrix[row][col]
                # tmp2 = matrix[n-row][n-col]
                # matrix[n-row][n-col] = tmp
                # tmp3 = matrix[n-row][col]
                # matrix[n-row][col] = tmp2
                # matrix[row][col] = tmp3
                # print (matrix)
        return matrix
            