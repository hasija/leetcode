# [3,4,1,5,7,6,2]
# Target 7
import copy
target = 1
nums = [3,4,1,5,7,6,2,8,9,10]
counter = 0
output = []
def recurse(nums, res=[]):
    global counter
    for x in range(len(nums)):
        if len(res)==0:
            print (x)
           
            # print (res)
            # print (f"Res before recurse: {res}")
            recurse(nums[x+1:], [nums[x]])
            # print (f"before debit: {res}")
            # print (f"after debit: {res}")
        if len(res)==1:
            # res.append(nums[x])
            print (res)
            recurse(nums[x+1:], res+[nums[x]])
            print (f"after: {res}")
        if len(res)==2:
            res.append(nums[x])
            # print (res)
            if sum(res)<target:
                output.append(res)
                counter+=1
            recurse(nums[x+1:], res)
        if len(res)==3:
            res[-1]=nums[x]
            # print(res)
            if sum(res)<target:

                if res in output:
                    pass
                else:
                    # print (res, sum(res))
                    output.append(copy.deepcopy(res))
                    counter+=1
            recurse(nums[:x]+nums[x+1:], res)

recurse(nums,[])
print(output, counter)
counter=0
nums.sort()
print (nums)
def sliding():
    global counter
    for k in range(len(nums)-2):
        first_val = nums[k]
        z = len(nums)-1
        # for x in range(len(nums[k+1:])):
        two_start=k+1
        while(two_start<len(nums)):
            if z>two_start:
                pass
            else:
                # two_start+=1
                # z=len(nums)-1
                # continue
                break
            if first_val+nums[two_start]+nums[z]<target:
                print (nums[k],nums[two_start], nums[z])
                print (first_val+nums[two_start]+nums[z])
                counter+=z-(two_start)
                output.append([first_val,nums[two_start],nums[z]])
                two_start+=1
                z=len(nums)-1
                continue
            z-=1
sliding()
print ("ans1")
print (counter,output)


new_counter=0
out_arr = []
def iteration():
    global new_counter
    for first in range(len(nums)):
        for second in range(first+1,len(nums)):
            for thrid in range(second+1,len(nums)):
                # print (thrid)
                # print (nums[first],nums[second],nums[thrid])
                if nums[first]+nums[second]+nums[thrid]<target:
                    new_counter+=1
                    out_arr.append([nums[first],nums[second],nums[thrid]])
iteration()
print ("ans2")
print (new_counter,out_arr)













