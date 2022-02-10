class Solution:
    def trailingZeroes(self, n: int) -> int:
        old_n = n
        final_num=n
        while n!=1 and n!=0:
            final_num*=n-1
            n-=1
        count=0
        for x in reversed(str(final_num)):
            if x=='0':
                count+=1
            else:
                break
        if old_n ==0:
            return 0
        return count