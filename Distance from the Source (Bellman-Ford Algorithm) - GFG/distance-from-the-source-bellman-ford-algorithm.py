#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        dist = [10**8 for _ in range(V)]
        dist[S] = 0
        for i in range(V-1):
            for E in adj:
                if dist[E[1]] > dist[E[0]] + E[2]:
                    dist[E[1]] = dist[E[0]] + E[2]
        
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
        adj = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends