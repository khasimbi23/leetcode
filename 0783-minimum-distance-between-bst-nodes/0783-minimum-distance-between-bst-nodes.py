# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.mini=float('inf')
        self.prev=None
        def helper(root):
            if root==None:
                return 
            helper(root.left)
            if self.prev!=None:
                self.mini=min(self.mini,root.val-self.prev.val)
            self.prev=root
            helper(root.right)
        helper(root)
        return self.mini
        