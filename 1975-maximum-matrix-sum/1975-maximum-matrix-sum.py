class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        neg_count = 0
        min_abs = float('inf')
        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(val))
        if neg_count % 2 == 1:
            total -= 2 * min_abs
        return total