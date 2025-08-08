class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        List=[[]*len(matrix) for _ in range(len(matrix))]
        for u in range(len(matrix)):
            for v in range(len(matrix)):
                if matrix[u][v]==1 and u!=v:
                    List[u].append(v)
                    List[v].append(u)
        visited=[False]*len(matrix)
        pro=0
        def bfs(node):
            q=deque()
            q.append(node)
            visited[node]=True
            while q:
                i=q.popleft()
                for neigh in List[i]:
                    if not visited[neigh]:
                        q.append(neigh)
                        visited[neigh]=True
        for i in range(len(List)):
            if not visited[i]:
                bfs(i)
                pro+=1
        return pro
        

        