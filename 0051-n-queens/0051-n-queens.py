class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col = set()
        dia1 = set()
        dia2 = set()
        def backtracking(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return 
            for c in range(n):
                if c in col or (r + c) in dia1 or (r - c) in dia2:
                    continue
                board[r][c] = "Q"
                col.add(c)
                dia1.add(r + c)
                dia2.add(r - c)
                backtracking(r + 1)
                board[r][c] = "."
                col.remove(c)
                dia1.remove(r + c)
                dia2.remove(r - c)  
        backtracking(0)
        return res