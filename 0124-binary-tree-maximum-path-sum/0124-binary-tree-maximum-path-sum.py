# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root,maxi):
            if root==None:
                return 0
            left=max(0,helper(root.left,maxi))
            right=max(0,helper(root.right,maxi))
            maxi[0]=max(maxi[0],root.val+left+right)
            return root.val+max(left,right)
        maxi=[float('-inf')]
        helper(root,maxi)
        return maxi[0]
         