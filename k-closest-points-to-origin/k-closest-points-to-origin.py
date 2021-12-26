import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []
        for point in points:
            li.append([point[0]**2 + point[1]**2,point])
        heapq.heapify(li)
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(li)[1])
        return ans
            
        