class Solution:
    def hammingWeight(self, n: int) -> int:
        sums=0
        k=bin(n)
        for i in k:
            if i=='1':
                sums=sums+1
        return sums