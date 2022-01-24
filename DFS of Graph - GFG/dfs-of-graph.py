#User function Template for python3
def dfs(u,adj):
    dfs.ans.append(u)
    for i in adj[u]:
        if not dfs.vis[i]:
            dfs.vis[i] = 1
            dfs(i,adj)
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        dfs.vis = [0 for _ in range(V)]
        dfs.ans = []
        for i in range(V):
            if not dfs.vis[i]:
                dfs.vis[i] = 1
                dfs(i,adj)
        return dfs.ans

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends