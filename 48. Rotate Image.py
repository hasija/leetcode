import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tmp = copy.deepcopy(matrix)
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                tmp[y][len(matrix)-1-x] = matrix[x][y]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                matrix[x][y]=tmp[x][y]
        return matrix




import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if y>x-1:
                    tmp = matrix[y][x]
                    matrix[y][x]=matrix[x][y]
                    matrix[x][y] = tmp
        # Rotate Array
        
        for x in range(len(matrix)):
            z= len(matrix)-1
            for y in range(len(matrix)//2+1):
                if z>=y:
                    tmp=matrix[x][z]
                    matrix[x][z]=matrix[x][y]
                    matrix[x][y]=tmp
                    z-=1