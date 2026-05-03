class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i, row in enumerate(matrix):
            prefix = 0
            for j, column in enumerate(row):
                prefix += matrix[i][j]
                prev_row = self.sum_matrix[i][j+1]
                self.sum_matrix[i+1][j+1] = prefix + prev_row

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = self.sum_matrix[row2+1][col2+1]
        minus_l = self.sum_matrix[row2+1][col1]
        minus_u = self.sum_matrix[row1][col2+1]
        add_duplicate = self.sum_matrix[row1][col1]
        return total_sum - minus_l - minus_u + add_duplicate


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)