class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s=sum(machines)
        n=len(machines)
        if s%n!=0:
            return -1
        target=s//n
        dif=0
        c_dif=0
        maxi=0
        for i in range(n):
            dif=machines[i]-target
            c_dif=c_dif+dif
            maxi=max(maxi,abs(c_dif),dif)
        return maxi