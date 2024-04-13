class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h_arr = [0]*(len(matrix[0])+1)
        m_area = 0
        for r_ind, row in enumerate(matrix):
            for ind, c in enumerate(row):
                if c =='1':
                    h_arr[ind]+=1
                else:
                    h_arr[ind] = 0
            stack = []
            # print ('row',r_ind,'height',h_arr)
            for ind, h in enumerate(h_arr):
                while (stack and h_arr[stack[-1]]>=h):
                    curr_h = h_arr[stack.pop()]
                    curr_w = ind if not stack else (ind-stack[-1]-1)
                    # print ("curr ind", ind, )
                    curr_area = curr_w*curr_h
                    m_area = max(m_area, curr_area)
                stack.append(ind)
            # print ("max area", m_area)
        return m_area