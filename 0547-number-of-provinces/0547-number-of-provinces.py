class Solution:
    def dfs(self,adj,node,visited):
        visited[node]=True
        for j in adj[node]:
            if not visited[j]:
                self.dfs(adj,j,visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict
        adj=defaultdict(list)
        rows=colns=len(isConnected)
        for i in range(rows):
            for j in range(colns):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        visited=[False]*rows
        count=0
        for i in range(rows):
            if not visited[i]:
                self.dfs(adj,i,visited)
                count+=1 
        return count


        


        
        