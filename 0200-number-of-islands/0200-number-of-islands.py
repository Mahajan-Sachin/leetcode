class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visited=[[False]*cols for _ in range(rows)]

        def bfs(row,col):
            q=deque()
            q.append((row,col))
            visited[row][col]=True
            while q:
                r,c=q.popleft()
                directions=[(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    new_row=r+dr
                    new_col=c+dc
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]=="1" and not visited[new_row][new_col]:
                        q.append((new_row,new_col))
                        visited[new_row][new_col]=True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and not visited[i][j]:
                    bfs(i,j)
                    islands+=1
        return islands
        