class Solution:
    def spiralOrder(self, n: List[List[int]]) -> List[int]:
        b_r = [0, len(n)]
        b_c = [0, len(n[0])]
        out = []
        while True:
            r = b_r[0]
            for c in range(b_c[0], b_c[1]):
                out.append(n[r][c])
            
            if b_r[1]-b_r[0]>1:
                
                c=b_c[1]-1
                for r in range(b_r[0]+1, b_r[1]):
                    out.append(n[r][c])
                r= b_r[1]-1
                
                if b_c[1]-b_c[0]>1:
                    
                    for c in range(b_c[1]-2, b_c[0]-1, -1):
                        # print ("appended")
                        out.append(n[r][c])

                    c = b_c[0]

                    for r in range(b_r[1]-2, b_r[0], -1):
                        out.append(n[r][c])

            curr_c = b_c[0]
            # print (out, 'iteration done')
            # print (b_r, b_c)
            if b_c[0]+1>=b_c[1]-1 or b_r[0]+1>=b_r[1]-1:
                return out
            else:
                b_r = [b_r[0]+1, b_r[1]-1]
                b_c = [b_c[0]+1, b_c[1]-1]