class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def get_next(num, move=None):            
            int_arr = str(num)
            len_ = len(int_arr)
            first = int(int_arr[0])
            if move is None and first+len_>9:
                first = 0
                len_+=1
            elif move == 'prev' and first+len_-1>9:
                first = 0
                len_+=1
                move = None
                
                
            if move is None:
                final = int(''.join([str(first+i) for i in range(1, len_+1)]))
            elif move == 'prev':
                final = int(''.join([str(first+i) for i in range(0, len_)]))
            # print (int_arr, first, len_)
            # print ('final',final)
            return final

        # 3 Cases
        # Normal move with one next
        # current move 
        # nine at last
        
        num = get_next(low, 'prev')
        # print ("FIRST", num)
        if num<low:
            num = get_next(num)
            # print ("Secondd", num)  
        ans = []
        
        while num<=high:
            ans.append(num)
            num = get_next(num)
        return ans

    


