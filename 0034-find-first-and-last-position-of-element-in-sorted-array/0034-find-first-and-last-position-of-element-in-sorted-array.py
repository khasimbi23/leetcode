class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not  nums:
            return [-1,-1]
        def find_first():
            left=0
            right=len(nums)-1
            ans=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
                if nums[mid] == target:
                    ans = mid
            return ans
        
        def find_last():
            left=0
            right=len(nums)-1
            ans=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<=target:
                    left = mid+1
                else:
                    right=mid-1
                if nums[mid] == target:
                    ans = mid
            return ans
        return [find_first(),find_last()]

