class Solution:
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap_nums():
            y = len(nums)-1
            for x in range(len(nums)):
                if x>=y:
                    break
                tmp = nums[x]
                nums[x] = nums[y]
                nums[y] = tmp
                y-=1
        break_point = None
        smallest_one = None
        smallest_num = -1
        for x in range(len(nums)-2, -1, -1):
            if nums[x]>=nums[x+1]:
                pass
            else:
                break_point = x
                break_num = nums[x]
                for y in range(x+1,len(nums)):
                    if nums[y]>break_num:
                        smallest_num = nums[y]
                        smallest_one = y
                    else:
                        break
                break
        if break_point is not None:
            tmp = nums[break_point]
            nums[break_point] = smallest_num
            nums[smallest_one] = tmp
            nums[break_point+1:] = nums[::-1][:len(nums)-break_point-1]
        else:
            swap_nums()
        return nums