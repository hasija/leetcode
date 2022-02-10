import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in range(len(nums)):
            if nums[x] in freq:
                freq[nums[x]]+=1
            else:
                freq[nums[x]] = 1

        nums = list(freq.keys())
        left = 0
        right = len(nums)-1
        desire_posi = len(nums)-k
        pivot_posi = random.randrange(len(nums))
        # print ("pivot",pivot_posi)        
        def quick_select(left, right, pivot_posi):
            store_ind = left
            match_freq = freq[nums[pivot_posi]]
            nums[right],nums[pivot_posi]=nums[pivot_posi],nums[right]
            for x in range(left, right+1):
                # print (freq[nums[x]],match_freq)
                if freq[nums[x]]<match_freq:
                    tmp = nums[x]
                    nums[x]=nums[store_ind]
                    nums[store_ind]=tmp
                    store_ind+=1
                else:
                    pass
            nums[right],nums[store_ind]=nums[store_ind],nums[right]
            # print (nums)
            if store_ind == desire_posi:
                return nums[desire_posi:]
                # print ("output",nums[desire_posi:])
            elif (desire_posi<store_ind):
                pivot_posi = random.randrange(left, store_ind)
                return quick_select(left,store_ind-1,pivot_posi)
            else:
                pivot_posi = random.randrange(store_ind+1, right+1)
                return quick_select(store_ind+1,right,pivot_posi)
                
        return quick_select(left,right,pivot_posi)
                
            