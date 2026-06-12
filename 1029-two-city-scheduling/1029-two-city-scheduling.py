class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        s=0
        x=len(costs)
        n=x//2
        for i in range(0,n):
            s=s+costs[i][0]
        for i in range(n,x):
            s=s+costs[i][1]
        return s