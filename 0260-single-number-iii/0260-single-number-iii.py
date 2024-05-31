class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        zor = 0
        for i in nums:
            zor^=i
        all_zor = zor
        all_zor_s = bin(all_zor)
        set_bit = None
        # print ("ALL ZOR", all_zor_s)
        for idx, bit in enumerate(reversed(all_zor_s)):
            if bit =='1':
                set_bit = idx
                break

        # print ("set bit", set_bit)
        for i in nums:
            if i&1<<set_bit:
                zor^=i
            
        # print (zor,all_zor^zor)
        ans = [zor, all_zor^zor]
        return ans