class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_count = len(matrix)
        col_count = len(matrix[0])
        rows = [False] * row_count
        cols = [False] * col_count
        is_empty = True
        
        
        for i in range(row_count):
            for j in range(col_count):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
                    is_empty = False
        
        
        if not is_empty:
            for i in range(row_count):
                for j in range(col_count):
                    if rows[i] or cols[j]:
                        matrix[i][j] = 0
        