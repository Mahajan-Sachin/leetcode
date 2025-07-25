class Solution:
    def List_conversion(self,matrix):
        n=len(matrix)
        List=[[] for _ in range(n)]
        for u in range(n):
            for v in range(u+1,n):
                if matrix[u][v]==1:
                    List[u].append(v)
                    List[v].append(u)
        return List
    def Bfs(self,start,adj_list,visited):
        q=deque()
        q.append(start)
        visited[start]=True
        while q:
            node=q.popleft()
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour]=True
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list=self.List_conversion(isConnected)
        province=0
        visited=[False]*len(adj_list)
        for i in range(len(adj_list)):
            if not visited[i]:
                self.Bfs(i,adj_list,visited)
                province+=1
        return province