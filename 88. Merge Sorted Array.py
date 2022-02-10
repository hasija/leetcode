class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_arr=[]
        head_1=0
        if len(nums2)>0:
            head_2=0
        else:
            head_2=None
        for x in range(len(nums1)):
            print (x)
            if head_1 is not None and head_2 is not None and head_1<(len(nums1)-len(nums2)):
                if nums1[head_1]>nums2[head_2]:
                    new_arr.append(nums2[head_2])
                    if head_2<len(nums2)-1:
                        head_2+=1
                    else:
                        head_2=None
                else:
                    new_arr.append(nums1[head_1])
                    if head_1<len(nums1)-1:
                        head_1+=1
                    else:
                        head_1=None
            elif head_1>=(len(nums1)-len(nums2)):
                new_arr.append(nums2[head_2])
                head_2+=1
            elif head_2 is None:
                new_arr.append(nums1[head_1])
                head_1+=1
            print (new_arr)
        for idx, val in enumerate(new_arr):
            nums1[idx]=val
                