"""
Maintain an array which contains all the stops.
Basically this array contains the net num passengers at ith position.
suppose there is a trip with [3,1,3] declared 0 index array becomes [0,3,0,-3]

At last start calculating sum of the array by iterating upto 1001 at any point if it exceeds capacity then return false.

"""
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
            