class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source=image[sr][sc]
        rows,cols=len(image),len(image[0])
        if image[sr][sc]==color:
            return image
        q=deque()
        q.append((sr,sc))
        image[sr][sc]=color
        while q:
            row,col=q.popleft()
            directions=[[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                new_row=dr+row
                new_col=dc+col
                if 0<=new_row<rows and 0<=new_col<cols and image[new_row][new_col]==source:
                    image[new_row][new_col]=color
                    q.append((new_row,new_col))
        return image 
        
        