class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        l1=[1]*n
        l1[0]=0
        l1[1]=0
        for i in range(2,int(n**0.5)+1):
            if(l1[i]==True):
                for j in range(i*i,n,i):
                    l1[j]=0
        return sum(l1)
        