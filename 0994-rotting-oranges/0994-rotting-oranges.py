class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        d=deque()
        fresh=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    d.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
        minutes=0
        while d and fresh!=0:
            for k in range(len(d)):
                x,y=d.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for i,j in directions:
                    nr,nc=x+i,j+y
                    if 0<=nr<r and 0<=nc<c and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        d.append([nr,nc])
            minutes+=1
        if fresh!=0:
            return -1
        else:
            return minutes
