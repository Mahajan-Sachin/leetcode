class Solution:
    def solve_board(self,row,board,n,cols,diag1,diag2,result):
        if row==n:
            snapshot=["".join(row) for row in board]
            result.append(snapshot)
            return
        for col in range(n):
            if col in cols or row-col in diag1 or row+col in diag2:
                continue
            board[row][col]="Q"
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            self.solve_board(row+1,board,n,cols,diag1,diag2,result)
            #backtrack
            board[row][col]="."
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=[["."]*n for _ in range(n)]
        row=set()
        cols=set()
        diagn_left=set()
        diagn_right=set()
        #hypothesis one row exist(small input)
        self.solve_board(0, board, n, cols, diagn_left, diagn_right, result)
        return result