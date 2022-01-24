def dfs(u,graph,color):
    curr = True
    for i in graph[u]:
        if dfs.vis[i] == 0:
            dfs.vis[i] = color
            curr = curr  and dfs(i,graph,-1*color)
        elif dfs.vis[i] == -1*color:
            return False
    return curr
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        dfs.vis = [0 for _ in range(n)]
        ans = True
        for i in range(n):
            if dfs.vis[i] == 0:
                dfs.vis[i] = 1
                ans = ans and dfs(i,graph,-1)
        return ans