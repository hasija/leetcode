class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # new_set=set(s)
        # new_set2=set(t)
        # x1=[True for x in t if x not in new_set]
        # x2=[True for x in s if x not in new_set2]
        # if len(x1)>0 or len(x2)>0 or len(s)!=len(t):
        #     return False
        # else:
        #     return True
        dict1={}
        for x in s:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        dict2={}
        for x in t:
            if x in dict2:
                dict2[x]+=1
            else:
                dict2[x]=1
        if dict1==dict2:
            return True
        else:
            return False