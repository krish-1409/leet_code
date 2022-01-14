class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0] )
        curr_max = points[0][1]
        ans = 1
        n = len(points)
        
        for i in range(1,n):
            if points[i][0]<=curr_max:
                curr_max = min(curr_max,points[i][1])
            else:
                ans+=1
                curr_max = points[i][1]
        return ans
                