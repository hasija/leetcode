class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        dim = len(img1)
        max_shift = 0
        
        def check_shifts_match(x1,y1, a, b):
            # print(x1,y1, 'start')
            match_left = 0
            match_right = 0
            for r_new in (range(y1, dim)):
                for y_new in (range(x1, dim)):
                    r_old = r_new-y1
                    y_old = y_new-x1
                    # print ("loooing", r_old, y_old ,a[r_new][y_new],  b[r_old][y_old])
                    if a[r_new][y_old] and b[r_old][y_new]:
                        # print ("match found")
                        match_left+=1
                    if a[r_new][y_new] and b[r_old][y_old]:
                        match_right+=1
            # print('matched', match)
            return max(match_left,match_right)
                    
        
        
        for y_shift in range(0,dim):
            for x_shift in range(0,dim):
                max_shift = max(check_shifts_match(x_shift, y_shift, img1, img2), max_shift)
                max_shift = max(check_shifts_match(x_shift, y_shift, img2, img1), max_shift)
        return max_shift
        