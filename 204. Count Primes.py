import math
class Solution:
    def countPrimes(self, n: int) -> int:
        prime_num=set()
        non_prime=set()
        for x in range(n):
            if x in non_prime:
                continue
            if x<2:
                continue
            if self.check_prime(x):
                prime_num.add(x)
            
            i=x**2
            while(i<n):
                counter=1
                if i not in non_prime:
                    non_prime.add(i)
                counter+=1
                i=i*counter
        return len(prime_num)
    def check_prime(self, t):
        y=2
        while y**2<=t:
            if t%y==0:
                return False
            y+=1
        return True


class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        arr=[True for i in range(n)]
        arr[0]=False
        arr[1]=False
        for x in range(2,int(n**0.5)+1):
            if arr[x] is False:
                continue
            # counter=x
            # while(x*counter<n):
            #     arr[x*counter]=False
            #     counter+=1
            for i in range(x*x,n,x):
                arr[i]=False
        # new_arr=[True for x in arr if x==True]
        return sum(arr)