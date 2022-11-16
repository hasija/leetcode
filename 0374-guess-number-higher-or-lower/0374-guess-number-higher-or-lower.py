# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        out = None
        mid = None
        while start<=end:
            # print (mid, out)
            mid = (start+end)//2
            out = guess(mid)
            if out>0:
                start = mid+1
            elif out<0:
                end = mid-1
            else:
                return mid
        # return start