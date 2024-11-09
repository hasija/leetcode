class Solution:
    def minEnd(self, n: int, x: int) -> int:
        min_bit = list(bin(x)[2:][::-1])
        LEN = len(min_bit)
        idx_arr = []
        last = x
        
        def find_all_zero_bit():
            cnt = 0
            for idx, i in enumerate(min_bit):
                if i == '0':
                    cnt+=1
                    idx_arr.append(idx)
            return cnt
        cnt = find_all_zero_bit()
        n_bits = bin(n-1)[2:][::-1]
        # print (n_bits)
        LEN = len(idx_arr)
        # print("len of idx arr", LEN, idx_arr)
        for idx, i in enumerate(n_bits):
            if i=='1':
                if idx<LEN:
                    # print ("here1")
                    min_bit[idx_arr[idx]]='1'
                else:
                    # print ("here2")
                    min_bit.append('1')
            else:
                if idx>=LEN:
                    # print ("here3")
                    min_bit.append('0')
        # print (''.join(min_bit[::-1]))
        return int(''.join(min_bit[::-1]),2)

            
            
            