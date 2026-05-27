class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def is_integer(val) -> bool:
            try:
                int(val)
                return True
            except Exception:
                return False
        res = []
        for op in operations:
            if is_integer(op):
                res.append(int(op))
            else:
                match op:
                    case '+':
                        res.append(res[-1] + res[-2])
                    case 'D':
                        res.append(res[-1]*2)
                    case 'C':
                        res.pop()
            print(res)
        s = 0
        for num in res:
            s += num
        return s