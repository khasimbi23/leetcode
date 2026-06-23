class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def backtracking(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + backtracking(i + 1, j + 1)
            else:
                memo[(i, j)] = max(backtracking(i + 1, j), backtracking(i, j + 1))
            return memo[(i, j)]
        return backtracking(0, 0)