import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist = [float('inf') for _ in range(V)]
        dist[S] = 0
        queue = [[0,S]]
        heapq.heapify(queue)
        
        while queue:
            u = heapq.heappop(queue)
            for v in adj[u[1]]:
                if dist[v[0]]>dist[u[1]]+v[1]:
                    dist[v[0]] = dist[u[1]]+v[1]
                    heapq.heappush(queue,[dist[v[0]],v[0]])
        
        return dist
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends