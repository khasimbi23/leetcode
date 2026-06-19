class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtracking(i, cur_expr, cur_val, prev_val):
            if i == len(num):
                if cur_val == target:
                    res.append(cur_expr)
                return
            
            for j in range(i, len(num)):
                if i != j and num[i] == "0":
                    break
                
                cur_str = num[i:j+1]
                cur_int = int(cur_str)
                
                if i == 0:
                    backtracking(j + 1, cur_str, cur_int, cur_int)
                else:
                    backtracking(j + 1, cur_expr + "+" + cur_str, cur_val + cur_int, cur_int)
                    backtracking(j + 1, cur_expr + "-" + cur_str, cur_val - cur_int, -cur_int)
                    backtracking(j + 1, cur_expr + "*" + cur_str, cur_val - prev_val + (prev_val * cur_int), prev_val * cur_int)
        
        backtracking(0, "", 0, 0)
        return res