class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            if i<0 or j<0 or j>=c or i>=r or board[i][j]!="O":
                return
            board[i][j]="E" 
            for x,y in [[1,0],[-1,0],[0,-1],[0,1]]:
                nr,nc=i+x,j+y
                dfs(nr,nc)
        r=len(board)
        c=len(board[0])
        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for i in range(c):
            dfs(0,i)
            dfs(r-1,i)
        for i in range(r):
            for j in range(c):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="E":
                    board[i][j]="O" 