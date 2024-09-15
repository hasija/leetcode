class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        xor_map = {0:-1}
        last = 0
        last_diff = 0
        max_ = 0
        char_map = [0]*26
        char_map[ord('a')-ord('a')]=1
        char_map[ord('e')-ord('a')]=2
        char_map[ord('i')-ord('a')]=4
        char_map[ord('o')-ord('a')]=8
        char_map[ord('u')-ord('a')]=16
        for idx, i in enumerate(s):
            last = last^char_map[ord(i)-ord('a')]
            if last in xor_map:
                max_ = max(idx-xor_map[last],max_)
            else:
                xor_map[last] = idx
        return max_