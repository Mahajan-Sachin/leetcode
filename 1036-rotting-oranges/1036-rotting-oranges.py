from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
            time += 1

        return time - 1 if fresh == 0 else -1
