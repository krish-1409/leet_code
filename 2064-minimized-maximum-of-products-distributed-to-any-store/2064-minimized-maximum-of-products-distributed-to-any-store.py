def numHouses(x,q):
    ans = 0
    for eachQuant in q:
        ans += ceil(eachQuant/x)
    return ans



class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        max_allot = max(quantities)
        min_allot = 1
        
        while min_allot<max_allot:
            x = (min_allot + max_allot)//2
            if numHouses(x,quantities) <= n:
                max_allot = x
            else:
                min_allot = x + 1
        
        return max_allot