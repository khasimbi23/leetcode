from collections import deque
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d1 = defaultdict(list)
        d = deque([[root, 0, 0]])  
        while d:
            node, row, col = d.popleft()
            d1[col].append([row, node.val])
            if node.left:
                d.append([node.left, row + 1, col - 1])
            if node.right:
                d.append([node.right, row + 1, col + 1])    
        res = []
        for key in sorted(d1.keys()):
            column_nodes = sorted(d1[key])
            column = [val for row, val in column_nodes]
            res.append(column)
            
        return res