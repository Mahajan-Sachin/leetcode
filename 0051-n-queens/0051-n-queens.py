class Solution:
    def isValid(self, board, row, col, n):
        # Check column above
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solve(self, board, row, result, n):
        if row == n:
            # Must deep copy row strings, not the board reference
            temp = ["".join(r) for r in board]
            result.append(temp)
            return

        for col in range(n):  # \U0001f41e you were using undefined 'col'
            if self.isValid(board, row, col, n):
                board[row][col] = 'Q'
                self.solve(board, row + 1, result, n)
                board[row][col] = '.'  # Backtrack

    def solveNQueens(self, n: int):
        result = []
        board = [["."] * n for _ in range(n)]
        self.solve(board, 0, result, n)
        return result
