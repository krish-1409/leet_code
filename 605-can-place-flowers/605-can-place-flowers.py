class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        n1 = len(flowerbed)
        ans = 0
        if n1==1:
            if flowerbed[0]==1 and n==0:
                return True
            elif flowerbed[0]==0 and n<=1:
                return True
            else:
                return False
        if flowerbed[0]==0 and flowerbed[1]==0:
            ans+=1
            flowerbed[0] = 1
        for i in range(1,n1-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                ans+=1
                flowerbed[i]=1
        if flowerbed[n1-2]==0 and flowerbed[n1-1]==0:
            ans+=1
        if ans>=n:
            return True
        return False
                