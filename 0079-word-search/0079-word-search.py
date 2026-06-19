class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        
        def backtracking(r, c, ind):
            if ind == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != word[ind]:
                return False
            
            temp = board[r][c]
            board[r][c] = "@" 
            ans = (backtracking(r + 1, c, ind + 1) or 
                   backtracking(r - 1, c, ind + 1) or 
                   backtracking(r, c - 1, ind + 1) or 
                   backtracking(r, c + 1, ind + 1))
            
            board[r][c] = temp   
            return ans
        
        for i in range(rows):
            for j in range(columns):
                if backtracking(i, j, 0):
                    return True
        return False