class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        prod1 = arr[0]
        prod2 = arr[0]
        ans = arr[0]
        for i in range(1,len(arr)):
            if arr[i]==0:
                prod1=1
                prod2=1
            temp = prod1
            prod1 = max(prod1*arr[i],max(arr[i],prod2*arr[i]))
            prod2 = min(prod2*arr[i],min(arr[i],temp*arr[i]))
            ans = max(ans,prod1)
        return ans
    # 2 3 -2 4
    