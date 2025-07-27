class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows=len(grid1)
        cols=len(grid1[0])
        visited=[[False]*cols for _ in range(rows)]
        islands=0
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visited[r][c]=True
            is_valid=True
            while q:
                row,col=q.popleft()
                if grid1[row][col]==0:
                    is_valid=False
                directions=[(0,-1),(0,1),(-1,0),(1,0)]
                for dr,dc in directions:
                    new_row=row+dr
                    new_col=col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and grid2[new_row][new_col]==1 and not visited[new_row][new_col]:
                        q.append((new_row,new_col))
                        visited[new_row][new_col]=True
            return is_valid
        islands=0        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c]==1 and not visited[r][c]:
                    if bfs(r,c):
                        islands+=1
        return islands
        