class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for x in range(len(height)):
            for y in range(len(height)-1, x, -1):
                if min(height[x], height[y])*(y-x)>max_area:
                    max_area= min(height[x], height[y])*(y-x)
        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        y= len(height)-1
        change_left=True
        change_right=False
        old_right = 0
        old_left = 0
        x=0
        while(x<y):
            if change_right:
                if old_left >= height[x]:
                    change_left = False
                    change_right = True
                    x+=1
                    continue
            if change_left:
                if old_right >= height[y]:
                    change_right = False
                    change_left = True
                    y-=1
                    continue
            tmp_area = (y-x)*min(height[x],height[y])
            if tmp_area>max_area:
                max_area = tmp_area
            elif height[x]<=height[y]:
                change_left = False
                change_right = True
                old_left = height[x]
                x+=1
                continue
            else:
                change_right = False
                change_left = True
                old_right = height[y]
                y-=1
                continue
        return max_area