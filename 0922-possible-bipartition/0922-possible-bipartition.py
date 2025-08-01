class Solution:
    def adj_list(self,n,edges):
        List=[[] for _ in range(n)]
        for u,v in edges:
            List[u-1].append(v-1)
            List[v-1].append(u-1)
        return List
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        List=self.adj_list(n,dislikes)
        color=[-1]*len(List)
        q=deque()
        for i in range(len(List)):
            if color[i]==-1:
                q.append(i)
                color[i]=0
                while q:
                    node=q.popleft()
                    for neighbour in List[node]:
                        if color[neighbour]==-1:
                            color[neighbour]=1-color[node]
                            q.append(neighbour)
                        elif color[neighbour]==color[node]:
                            return False
        return True


        