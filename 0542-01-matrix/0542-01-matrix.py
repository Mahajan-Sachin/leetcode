class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=-1
        while q:
            row,col=q.popleft()
            directions=[(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr,dc in directions:
                new_row=row+dr
                new_col=col+dc
                if 0<=new_row<m and 0<=new_col<n and mat[new_row][new_col]==-1:
                    mat[new_row][new_col]=mat[row][col]+1
                    q.append((new_row,new_col))
        return mat
