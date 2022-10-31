class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        flag = False
        for row in range(m):
            col = 0
            old = None
            while(row<m and col<n):
                if old is None:
                    old = matrix[row][col]
                    row+=1
                    col+=1
                    continue
                curr = matrix[row][col]
                row+=1
                col+=1
                if curr!=old:
                    flag=True
                    return False
        for col in range(n):
            row = 0
            old = None
            while(row<m and col<n):
                if old is None:
                    old = matrix[row][col]
                    row+=1
                    col+=1
                    continue
                curr = matrix[row][col]
                row+=1
                col+=1
                if curr!=old:
                    flag=True
                    return False
        if flag:
            return False
        return True