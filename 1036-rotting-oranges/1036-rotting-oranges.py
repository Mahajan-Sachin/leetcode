class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif(grid[i][j]==1):
                    fresh+=1
        if fresh==0:
            return 0
        minutes=-1
        while q:
            length=len(q)
            for _ in range(length):
                row,col=q.popleft()
                directions=[(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    new_row=dr+row
                    new_col=dc+col
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col]=2
                        fresh-=1
                        q.append((new_row,new_col))
            minutes+=1
        return minutes if fresh==0 else -1
        

                 
        