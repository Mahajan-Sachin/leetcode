class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        source=image[sr][sc]
        q=collections.deque()
        if image[sr][sc]==color:
            return image
        q.append((sr,sc))
        image[sr][sc]=color
        while q:
            r,c=q.popleft()
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in directions:
                new_row=r+dr
                new_col=c+dc
                if 0<=new_row<rows and 0<=new_col<cols and image[new_row][new_col]==source:
                    image[new_row][new_col]=color
                    q.append((new_row,new_col))
        
        return image
        