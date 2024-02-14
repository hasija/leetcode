class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi = deque()
        negi = deque()
        new_arr = []
        curr = '+'
        for i in nums:
            if i>0:
                posi.append(i)
            else:
                negi.append(i)
            if curr == '+' and posi:
                new_arr.append(posi.popleft())
                curr = '-'
            elif curr == '-' and negi:
                new_arr.append(negi.popleft())
                curr = '+'
        while negi or posi:
            if curr == '+' and posi:
                new_arr.append(posi.popleft())
                curr = '-'
            elif curr == '-' and negi:
                new_arr.append(negi.popleft())
                curr = '+'
        return new_arr