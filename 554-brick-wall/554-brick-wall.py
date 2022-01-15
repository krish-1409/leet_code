class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        m = sum(wall[0])
        
        """
        dic = [n for _ in range(m+1)]
        
        for i in range(n):
            temp = 0
            for brick in wall[i]:
                temp+=brick
                dic[temp]-=1
        dic[m] = n
        return min(dic)
        
        """
        dic = {}
        
        for i in range(n):
            temp = 0
            for brick in wall[i]:
                temp+=brick
                if temp not in dic:
                    dic[temp]=1
                else:
                    dic[temp]+=1
        
        ans = float('inf')
        for key,value in dic.items():
            if key!=m:
                ans = min(ans,n-dic[key])
        if ans==float('inf'):
            return n
        return ans