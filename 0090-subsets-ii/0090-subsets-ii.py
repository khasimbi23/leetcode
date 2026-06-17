class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(i,curr_subset):
            if i==len(nums):
                if curr_subset not in res:
                    res.append(curr_subset[:])
                return
            curr_subset.append(nums[i])
            backtrack(i+1,curr_subset)
            curr_subset.pop()
            backtrack(i+1,curr_subset)
        nums.sort()
        backtrack(0,[])
        return res