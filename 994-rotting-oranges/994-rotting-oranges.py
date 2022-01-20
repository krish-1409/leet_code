class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        n = len(grid)
        m = len(grid[0])
        rottenQ = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    rottenQ.append([i,j,0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        ans = 0
        while rottenQ:
            curr = rottenQ.pop(0)
            ans = max(ans,curr[2])
            for i,j in direction:
                if 0<=curr[0]+i<n and 0<=curr[1]+j<m and grid[curr[0]+i][curr[1]+j]==1 :
                    grid[curr[0]+i][curr[1]+j] = 2
                    rottenQ.append([curr[0]+i,curr[1]+j,curr[2]+1])
                    fresh-=1
                    
        return ans if fresh==0 else -1
                    
            