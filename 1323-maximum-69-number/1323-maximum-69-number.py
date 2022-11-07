class Solution:
    def maximum69Number (self, num: int) -> int:
        chars = str(num)
        for ind in range(len(str(num))):
            curr = chars[ind]
            if curr=='6':
                return int(chars[:ind]+'9'+chars[ind+1:])
        return num
                
        