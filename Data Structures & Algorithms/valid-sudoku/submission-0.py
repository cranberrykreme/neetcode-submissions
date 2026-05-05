class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if not item.isdigit():
                    continue
                if item in rows[i]:
                    return False
                if item in columns[j]:
                    return False
                square_row = (i // 3)*3
                square_col = j // 3
                square = square_row + square_col
                if item in squares[square]:
                    return False
                rows[i].add(item)
                columns[j].add(item)
                squares[square].add(item)
        return True
