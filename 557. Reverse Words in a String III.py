class Solution:
    def reverseWords(self, s: str) -> str:
        new_arr=s.split(' ')
        for i in range(len(new_arr)):
            new_arr[i]=new_arr[i][::-1]

        return ' '.join(new_arr)
        