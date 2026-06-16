class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        l=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                l[i]=l[i-1]+1
        s=l[n-1]
        cur=1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                cur+=1
            else:
                cur=1
            s=s+max(l[i],cur)
        return s
#t.c=o(2n)
#s.c=o(n)
        