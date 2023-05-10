class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        b_r = [0, n]
        b_c = [0 ,n]
        
        mat = [[0]*n for i in range(n)]
        counter = 1
        while True:
            r = b_c[0]
            for c in range(b_c[0], b_c[1]):
                mat[r][c]=counter
                counter+=1
            
            c = b_r[1]-1
            for r in range(b_r[0]+1, b_r[1]):
                mat[r][c]=counter
                counter+=1
            
            r = b_r[1]-1
            
            for c in range(b_c[1]-2, b_c[0]-1, -1):
                mat[r][c]=counter
                counter+=1
            
            c = b_c[0]
            for r in range(b_r[1]-2, b_r[0], -1):
                mat[r][c]=counter
                counter+=1
            
            b_r = [b_r[0]+1, b_r[1]-1]
            b_c = [b_c[0]+1, b_c[1]-1]
            # print (mat)
            # print (b_r, b_c)
            if b_c[0]>=b_c[1] or b_r[0]>=b_r[1]:
                return mat
            
                
        