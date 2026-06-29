class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        grid=[[float('inf')]*n for i in range(n)]
        for i in range(n):
            grid[i][i]=0
        for u,v,w in edges:
            grid[u][v]=w
            grid[v][u]=w
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    grid[i][j]=min(grid[i][j],grid[i][via]+grid[via][j])
        mini=float('inf')
        res_city=-1
        for i in range(n):
            c=0
            for j in range(n):
                if grid[i][j]<=distanceThreshold:
                    c+=1
            if c<=mini:
                mini=c
                res_city=i
        return res_city
                    