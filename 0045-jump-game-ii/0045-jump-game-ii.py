class Solution:
    def jump(self, nums: List[int]) -> int:
        maxi=0
        jumps=0
        dist=0
        for i in range(len(nums)-1):
            maxi=max(maxi,i+nums[i])
            if i==dist:
                jumps+=1
                dist=maxi
        return jumps