class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = list(reversed(bin((2**maximumBit)-1)[2:]))
        # print (max_val)
        n = len(nums)
        len_max = len(max_val)
        zors = 0
        def get_max_val(val):
            val = list(reversed(bin(val)[2:]))
            # print ("Check zor for val", val)
            ans_bit = ""
            for i in range(len_max):
                max_val_bit = max_val[i]
                if i<len(val):
                    if max_val_bit==val[i] == '0':

                        ans_bit+='0'
                    elif max_val_bit==val[i] == '1':

                        ans_bit+='0'
                    elif max_val_bit!=val[i] and val[i] == '1':

                        ans_bit+='0'
                    elif max_val_bit!=val[i] and val[i] == '0':

                        ans_bit+='1'
                else:
                    if max_val_bit == '0':

                        ans_bit+='0'
                    else:

                        ans_bit+='1'
            # print ("ans for curr", int(ans_bit[::-1],2))
            return int(ans_bit[::-1],2)
        ans = []
        for i in range(n):
            if i ==0:
                zors=nums[i]
                ans.append(get_max_val(zors))
                continue
            zors = zors^nums[i]
            ans.append(get_max_val(zors))
        return ans[::-1]