class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap = [0] * (1001)
        for trip in trips:
            cap[trip[1]] += trip[0]
            cap[trip[2]] -= trip[0]
        curr = 0
        for i in range(1001):
            curr += cap[i]
            if curr>capacity:
                return False
        return True
            