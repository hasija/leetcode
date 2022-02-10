class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         old_k = k
#         default_k = k
#         rotation = []
#         if k>=len(nums):
#             print("here")
#             while(True):
                
#         else:
#             for x in reversed(range(len(nums))):
#                 print(x)
#                 if k!=0:
#                     rotation.append(nums[x])
#                 if x>=default_k:
#                     nums[x]=nums[x-default_k]
#                     print (f"nums after: {nums}")
#                     k-=1
#                     continue
#                 else:
#                     nums[x]=rotation[0]
#                     rotation.pop(0)
        k=k%len(nums)
        if k==0:
            pass
        elif k<=len(nums):
            tmp=nums[-k:]
            print(tmp)
            nums[k:]=nums[:len(nums)-k]
            print(tmp)
            nums[:k]=tmp