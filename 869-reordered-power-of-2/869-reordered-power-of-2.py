class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        two_power = 2
        power_set = {1:{'1':1}}
        while two_power<=10**9:
            tmp_dict = collections.defaultdict(int)
            for k in str(two_power):
                tmp_dict[k]+=1
            power_set[two_power]=tmp_dict
            
            two_power*=2
        # print (two_power)
        # print (power_set)
        new_dict = collections.defaultdict(int)
        for k in str(n):
            new_dict[k]+=1
        # print (new_dict)
        for k,v in power_set.items():
            flag = True
            for k2,v2 in new_dict.items():
                if k2 in v and v[k2]==v2:
                    continue
                else:
                    # if n==1:
                    #     # print (k2, v, v2, 'running debug')
                    #     # print(k2 in v)
                    #     # print (v[k2]==v2)
                    flag=False
            # if n==1 or n==10:
            #     print ("printing len", flag)
            #     print (len(str(k)),k)
            #     print (len(str(n)), n)
            if flag and len(str(k))==len(str(n)):
                # print (k,v)
                return True
        return False