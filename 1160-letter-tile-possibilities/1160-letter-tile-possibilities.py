class Solution:
    def helper(self, tiles, curr, visited, count):
        for i in range(len(tiles)):
            if visited[i]:
                continue
            if i > 0 and tiles[i] == tiles[i - 1] and visited[i - 1]==False:
                continue
            visited[i] = True
            count[0] += 1  # Count this new sequence
            self.helper(tiles, curr + tiles[i], visited, count)
            visited[i] = False  # Backtrack

    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        count = [0]
        visited = [False] * len(tiles)
        self.helper(tiles, "", visited, count)
        return count[0]
