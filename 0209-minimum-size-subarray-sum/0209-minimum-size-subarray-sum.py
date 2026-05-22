class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        mini=float('inf')
        l=0
        s=0
        for r in range(len(nums)):
            s=s+nums[r]
            while (s>=target):
                mini=min(mini,r-l+1)
                s=s-nums[l]
                l=l+1
        if (mini == float('inf')):
            return 0
        else:
            return mini