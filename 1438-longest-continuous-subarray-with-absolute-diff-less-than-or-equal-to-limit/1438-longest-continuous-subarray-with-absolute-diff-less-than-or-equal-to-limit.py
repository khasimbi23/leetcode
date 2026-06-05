from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()
        l = 0
        maxi = 0
        for r in range(len(nums)):
            while max_dq and nums[max_dq[-1]] < nums[r]:
                max_dq.pop()
            max_dq.append(r)
            while min_dq and nums[min_dq[-1]] > nums[r]:
                min_dq.pop()
            min_dq.append(r) 
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                l += 1
                if max_dq[0] < l:
                    max_dq.popleft()
                if min_dq[0] < l:
                    min_dq.popleft() 
            maxi = max(maxi, r - l + 1)  
        return maxi