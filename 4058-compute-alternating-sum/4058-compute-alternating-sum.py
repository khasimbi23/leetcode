class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                ans += v
            else:
                ans -= v
        return ans