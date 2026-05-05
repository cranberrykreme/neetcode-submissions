class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if not item.isdigit():
                    continue
                if item in rows[i]:
                    return False
                if item in columns[j]:
                    return False
                square = (i // 3, j // 3)
                if item in squares[square]:
                    return False
                rows[i].add(item)
                columns[j].add(item)
                squares[square].add(item)
        return True
