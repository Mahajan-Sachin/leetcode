class Solution:
    def List_conversion(self,matrix):
        adj_list=[[] for _ in range(len(matrix))]
        for u in range(len(matrix)):
            for v in range(len(matrix)):
                if u!=v and matrix[u][v]==1: #ya u!=v islia kiya because we dont want to do redduncy because conneted means we want connections to another nodes, not itself
                    adj_list[u].append(v)
                    adj_list[v].append(u)
        return adj_list
    def bfs(self,start,visited,adj_list):
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
        visited=[False]*len(adj_list)
        count=0
        for i in range(len(adj_list)):
            if not visited[i]:
                self.bfs(i,visited,adj_list)
                count+=1
        return count
        
        