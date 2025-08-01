class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        area=0
        visited=[[False]*cols for _ in range(rows)]
        def bfs(i,j) ->int:
            q=deque()
            q.append((i,j))
            visited[i][j]=True
            Area=0
            while q:
                r,c=q.popleft()
                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    if (0 <= new_row < rows and 0 <= new_col < cols) and grid[new_row][new_col]==1 and not visited[new_row][new_col]:
                        Area+=1
                        q.append((new_row,new_col))
                        visited[new_row][new_col]=True
            return Area+1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and not visited[i][j]:
                    new_area=bfs(i,j)
                    area=max(area,new_area)
        return area
        