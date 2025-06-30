from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n
        start=source
        queue=deque()
        queue.append(start)
        visited[start]=True
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour]=True
        return False
        