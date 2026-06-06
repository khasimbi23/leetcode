class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi_dia = [0]
        def helper(root, max_dia_list):
            if root is None:
                return 0
            left = helper(root.left, max_dia_list)
            right = helper(root.right, max_dia_list)
            max_dia_list[0] = max(max_dia_list[0], left + right)
            return 1 + max(left,right)
        helper(root, maxi_dia)
        return maxi_dia[0]