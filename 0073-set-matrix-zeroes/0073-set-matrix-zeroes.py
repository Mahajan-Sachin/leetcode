class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        
        # Step 1: Store all rows and cols that contain 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Step 2: Zero out marked rows
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        
        # Step 3: Zero out marked columns
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
