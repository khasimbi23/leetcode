class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = deque([root])
        res = []
        while d:
            level = []
            for i in range(len(d)):
                node = d.popleft()
                level.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(level)
            
        return res