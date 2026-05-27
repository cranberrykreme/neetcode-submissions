class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res, s = [], 0
        for op in operations:
            match op:
                case '+':
                    s += res[-1] + res[-2]
                    res.append(res[-1] + res[-2])
                case 'D':
                    s += res[-1]*2
                    res.append(res[-1]*2)
                case 'C':
                    s -= res[-1]
                    res.pop()
                case _:
                    res.append(int(op))
                    s += res[-1]

        return s