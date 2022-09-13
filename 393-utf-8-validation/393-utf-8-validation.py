class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        start = True
        char_size = 0
        for val in data:
            bin_rep = format(val, '#010b')[-8:]
            if char_size==0:
                count=0
                char = bin_rep[0]
                if char=='0':
                    continue
                else:
                    while char!='0' and count<7:
                        count+=1
                        char=bin_rep[count]
                if count>4 or count==1:
                    return False
                char_size = count-1
                start=False
                continue
            else:
                if bin_rep[:2]!='10':
                    return False
                char_size-=1
        if char_size!=0:
            return False
        return True
    
# [197,130,1]
# [235,140,4]
# [197,130,197,130,235, 140, 140,1]
# [1, 197,130]