class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        rows = [False] * ROWS
        columns = [False] * COLUMNS

        for i in range(ROWS):
            for j in range(COLUMNS):
                if matrix[i][j] == 0:
                    rows[i] = True
                    columns[j] = True

        for i in range(ROWS):
            for j in range(COLUMNS):
                if rows[i] or columns[j]:
                    matrix[i][j] = 0        
        