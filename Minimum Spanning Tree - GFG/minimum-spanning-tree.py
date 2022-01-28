#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        mst = [0 for i in range(V)]
        parent = [-1 for i in range(V)]
        getMin = [[-1,-1,0]]
        heapq.heapify(getMin)
        # print(adj)
        while getMin:
            curr = heapq.heappop(getMin)
            if mst[curr[2]]!=1:
                mst[curr[2]] = 1
                parent[curr[2]] = curr[1]
                for i in adj[curr[2]]:
                    if mst[i[0]]==0:
                        heapq.heappush(getMin,[i[1],curr[2],i[0]])
        ans = 0
        for u in range(1,V):
            for v in adj[u]:
                if v[0]==parent[u]:
                    ans+=v[1]
                    break
        return ans
                
            
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends