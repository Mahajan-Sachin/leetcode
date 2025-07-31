class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows=len(maze)
        cols=len(maze[0])
        q=deque()
        enter_row=entrance[0]
        enter_col=entrance[1]
        steps=0
        q.append((enter_row,enter_col,steps))
        while q:
            row,col,step=q.popleft()
            if (row != entrance[0] or col != entrance[1]) and ((row == 0 or row == rows-1) or (col == 0 or col == cols-1)):
                return step
            directions=[[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                new_row=row+dr
                new_col=col+dc
                if 0<=new_row<rows and 0<=new_col<cols and maze[new_row][new_col]==".":
                    maze[new_row][new_col]="+"
                    q.append((new_row,new_col,step+1))
        return -1
        